import os
import json
import asyncio

import tornado.ioloop
import tornado.web
from tornado.options import define, options

from peewee import IntegrityError
from models import ItemList
from models import OutdatedError


def json_serialize(obj):
    return json.dumps(obj, indent=2, sort_keys=True, default=str, ensure_ascii=False).encode('utf8')

# define a port for serving requests. Heroku uses 5000
define("port", default=5000, help="run on the given port", type=int)


class Application(tornado.web.Application):
    """Основное приложение"""
    def __init__(self):
        handlers = self.get_handlers()
 
        settings = dict(
            cookie_secret='474446ad24ee5490f8e879012ee2a855a7c7bf56',
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            default_handler_class=My404Handler,
            #xsrf_cookies=True,
            #debug=True,
        )
        super(Application, self).__init__(handlers, **settings)

    def get_handlers(self):
        prefix = '/api/person'
        id_group = '(?P<item_id>[0-9]+)'
        action_group = '(?P<action>[a-z]+)'
        all_routes = [
            '{prefix}',
            '{prefix}/{action}',
            '{prefix}/{id}',
            '{prefix}/{id}/{action}',
        ]
        dist_path = os.path.join(os.path.dirname(__file__), 'dist')
        return [
            (r.format(prefix=prefix, id=id_group, action=action_group), CrudHandler)
            for r in all_routes] + [('/api/dpt', DptHandler),
            ('/(.*)', MainHandler, {'path': dist_path})]


class My404Handler(tornado.web.RequestHandler):
    """Отображение страницы с ошибкой"""
    def prepare(self):
        self.set_status(404, 'File not Found')
        self.render('404.html')


class BaseHandler(tornado.web.RequestHandler):
    """Базовый обработчик запросов."""
    def set_default_headers(self, *args, **kwargs):
        """предоставляет доступ к ресурсам с других доменов"""
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, PUT, DELETE, OPTIONS")


class MainHandler(tornado.web.StaticFileHandler):
    """Отображает главную страницу.
    предоставляет доступ к папке dist"""
    def parse_url_path(self, url_path):
        if not url_path or url_path.endswith('/'):
            url_path = url_path + 'index.html'
        return url_path


class DptHandler(BaseHandler):
    """возвращает список отделов"""
    def get(self):
        self.set_header('Content-Type', 'application/json')
        items = ItemList.get_dpt()
        response = json_serialize(items)
        self.write(response)


class CrudHandler(BaseHandler):
    """
    метод   путь                комментарий
    GET     {prefix}            отображает список элементов
    GET     {prefix}/{id}	    возвращает элемент по id
    PUT     {prefix}/{id}	    обновляет значение элемента
    DELETE  {prefix}/{id}	    удаляет элемент
    POST    {prefix}            добавляет новый элемент
    POST    {prefix}/{id}/delete    то же, что DELETE
    POST    {prefix}/{id}	    то же, что PUT
    """
    def get(self, item_id=None, action=None):
        """Обработка путей метода GET"""
        if action is not None:
            self.error404()
        else:
            if not item_id:
                #GET     {prefix}            отображает список элементов
                self.get_index()
            else:
                #GET     {prefix}/{id}	    возвращает элемент по id
                self.get_item(item_id)
            
    def post(self, item_id=None, action=None):
        """Обработка путей метода POST"""
        if not item_id:
            if not action:
                #POST    {prefix}            добавляет новый элемент
                self.create_item()
            else:
                self.error404()
        else:
            #item_id is set
            if not action:
                #POST    {prefix}/{id}	    то же, что PUT
                self.put(item_id)
            elif action == 'delete':
                #POST    {prefix}/{id}/delete    то же, что DELETE
                self.delete(item_id)
            else:
                self.error404()

    def put(self, item_id, action=None):
        """Обработка путей метода PUT"""
        if not item_id or action is not None:
            self.error404()
        else:
            #PUT     {prefix}/{id}	    обновляет значение элемента
            self.set_header('Content-Type', 'application/json')
            try:
                idx = int(item_id)
                req = { k: self.get_argument(k) for k in self.request.arguments }
                item = ItemList.update(idx, req)
                response = json_serialize(item)
                self.write(response)
            except IndexError as err:
                self.set_status(404, 'Item not found')
                self.write({'message': 'DoesNotExist'})
            except IntegrityError as err:
                self.set_status(405, 'Validation Exception')
                self.write({'message': 'DoesNotExist'})
            except OutdatedError as err:
                self.set_status(400, 'Item is outdated')
                self.write({'message': 'DoesNotExist'})

    def delete(self, item_id, action=None):
        """Обработка путей метода DELETE"""
        if not item_id or action is not None:
            self.error404()
        else:
            #DELETE  {prefix}/{id}	    удаляет элемент
            self.set_header('Content-Type', 'application/json')
            try:
                idx = int(item_id)
                response = ItemList.delete(idx)
                self.write({'message': 'OK'})
            except IndexError as err:
                self.set_status(404, 'Item not found')
                self.write({'message': 'DoesNotExist'})
            
    def error404(self):
        """Отображение страницы с ошибкой"""
        self.set_status(404, 'File not Found')
        self.render('404.html')

    def get_index(self):
        """Возвращает список всех сотрудников"""
        self.set_header('Content-Type', 'application/json')
        items = ItemList.get_index()
        response = json_serialize(items)
        self.write(response)

    def create_item(self):
        """Добавляет новый элемент"""
        self.set_header('Content-Type', 'application/json')
        try:
            req = { k: self.get_argument(k) for k in self.request.arguments }
            item = ItemList.create(req)
            response = json_serialize(item)
            self.write(response)
        except IntegrityError as err:
            self.set_status(405, 'Invalid input')
            self.write({'message': 'IntegrityError'})

    def get_item(self, item_id):
        """возвращает элемент по id"""
        self.set_header('Content-Type', 'application/json')
        try:
            idx = int(item_id)
            item = ItemList.get(idx)
            response = json_serialize(item)
            self.write(response)
        except IndexError as err:
            self.set_status(404, 'Item not found')
            self.write({'message': 'DoesNotExist'})


def main():
    """Основная петля событий"""
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

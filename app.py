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


define("port", default=8000, help="run on the given port", type=int)


class Application(tornado.web.Application):
    """Основное приложение"""
    def __init__(self):
        handlers = self.get_handlers()
 
        settings = dict(
            cookie_secret='__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__',
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            #xsrf_cookies=True,
            debug=True,
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
        return [
            (r.format(prefix=prefix, id=id_group, action=action_group), CrudHandler)
            for r in all_routes] + [('/', MainHandler), ('/api/dpt', DptHandler)]


class MainHandler(tornado.web.RequestHandler):
    """Отображает главную страницу"""
    def get(self):
        items = ItemList.get_index()
        self.render('index.html', items=items)

class DptHandler(tornado.web.RequestHandler):
    """возвращает список отделов"""
    def get(self):
        self.set_header('Content-Type', 'application/json')
        items = ItemList.get_dpt()
        response = json_serialize(items)
        self.write(response)


class CrudHandler(tornado.web.RequestHandler):
    """
    метод   путь                комментарий
    GET     {prefix}            отображает список элементов
    GET     {prefix}/add        возвращает форму для добавления нового элемента
    GET     {prefix}/{id}	    возвращает элемент по id
    GET     {prefix}/{id}/edit	отображает форму для редактирования элемента
    PUT     {prefix}/{id}	    обновляет значение элемента
    DELETE  {prefix}/{id}	    удаляет элемент
    POST    {prefix}            добавляет новый элемент
    POST    {prefix}/{id}/delete    то же, что DELETE
    POST    {prefix}/{id}	    то же, что PUT
    """
    def get(self, item_id=None, action=None):
        """Обработка путей метода GET"""
        if not item_id:
            if not action:
                #GET     {prefix}            отображает список элементов
                self.get_index()
            elif action == 'add':
                #GET     {prefix}/add        возвращает форму для добавления нового элемента
                self.form_add_item()
            else:
                self.error404()
        else:
            #item_id is set
            if not action:
                #GET     {prefix}/{id}	    возвращает элемент по id
                self.get_item(item_id)
            elif action == 'edit':
                #GET     {prefix}/{id}/edit	отображает форму для редактирования элемента
                self.form_edit_item(item_id)
            else:
                self.error404()
            
    def post(self, item_id=None, action=None):
        """Обработка путей метода POST"""
        if not item_id:
            if not action:
                #POST    {prefix}            добавляет новый элемент
                self.add_item()
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
        self.render('404.html')

    def form_add_item(self):
        dpts = ItemList.get_dpt()
        self.render('form.html', dpts=dpts)

    def form_edit_item(self, item_id):
        try:
            idx = int(item_id)
            item = ItemList.get(idx)
            dpts = ItemList.get_dpt()
            self.render('form.html', dpts=dpts, item=item)
        except IndexError as err:
            self.set_status(404, 'Item not found')
            self.write({'message': 'DoesNotExist'})

    def get_index(self):
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
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

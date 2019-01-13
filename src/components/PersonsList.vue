<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>

      <v-list two-line v-if="items.length">
        <ListItem
          v-for="item in items"
          :key="item.id"
          :item="item"
          @edit="editItem"
          @archive="archiveToggleItem"
        />
      </v-list>
      <p v-else>
        Список сотрудников пуст.
      </p>

      <v-btn color="red" dark fab bottom left fixed @click="$vuetify.goTo(0, { duration: 500, offset: 0 })">
          <v-icon>keyboard_arrow_up</v-icon>
      </v-btn>
      <v-btn color="pink" dark fab bottom right fixed @click="addItem">
          <v-icon>add</v-icon>
      </v-btn>
      <PersonForm
        @create="createItem"
        @update="updateItem"
        ref="add_form"/>
      <PersonForm
        edit_mode
        @create="createItem"
        @update="updateItem"
        @remove="removeItem"
        ref="edit_form"/>
      <Notice
        ref="snack"/>
    </v-layout>
  </v-container>
</template>

<script>
import ListItem from './ListItem'
import PersonForm from './PersonForm'
import Notice from './Notice'

export default {
  components: {
    ListItem, PersonForm, Notice
  },
  data: () => ({
    items: [],
  }),
  methods: {
		addItem () {
      this.$refs.add_form.show()
    },
    editItem (id) {
      this.$refs.edit_form.set(id)
      this.$refs.edit_form.show()
    },
    getFormData (item, reverse_birthday=true) {
      var formData = new FormData()
      for (const key of Object.keys(item)) {
          var val = item[key]
          if (reverse_birthday & key === 'birthday') {
            val = val.split('.').reverse().join('-')
          }
          // use key, val
          formData.append(key, val)
      }
      return formData
    },
    removeItem (item) {
      var url = 'person/' + item.id + '/delete'
      var formData = this.getFormData({id: item.id})
      var name = this.getName(item)
      // POST url
      this.$http.post(url, formData).then(response => {
        // success callback
        var notice = 'Сотрудник ' + name + ' удален'

        this.$refs.edit_form.show(false)
        this.popItem(item)
        this.showNotice('success', notice)
      }, response => {
        // error callback
        var notice = 'Ошибка сохранения сотрудника ' + name + '. Причина: ' + response.body.message
        this.showNotice('error', notice)
      });      
    },
    archiveToggleItem (id) {
      console.log('archiveToggleItem', id)
      var url = 'person/' + id
      this.$http.get(url).then(response => {
        // success callback
        var item = response.body
        item.dpt = item.dpt.id

        item.is_archive = !item.is_archive
        this.archivePostItem(item)
      }, response => {
          // error callback
      })
    },
    archivePostItem (item) {
      var url = 'person/' + item.id
      var dst = 'из архива'
      if (item.is_archive) {
        dst = 'в архив'
      }
      var formData = this.getFormData(item, false)
      // POST url
      this.$http.post(url, formData).then(response => {
        // success callback
        var notice = 'Сотрудник ' + name + ' перемещен ' + dst
        this.showNotice('success', notice)
        this.refreshItem(item)
      }, response => {
        // error callback
        var notice = 'Ошибка перемещения сотрудника ' + name + ' ' + dst + '. Причина: ' + response.body.message
        this.showNotice('error', notice)
      })      
    },
    createItem (item) {
      var formData = this.getFormData(item)
      var url = 'person'
      // POST url
      this.$http.post(url, formData).then(response => {
        // success callback
        var new_item = response.body
        var name = this.getName(new_item)
        var notice = 'Сотрудник ' + name + ' успешно создан'

        this.$refs.add_form.show(false)
        this.appendItem(new_item)
        this.showNotice('success', notice)
      }, response => {
        // error callback
        var notice = 'Ошибка создания сотрудника ' + name + '. Причина: ' + response.body.message
        this.showNotice('error', notice)
      });      
    },
    updateItem (item) {
      var url = 'person/' + item.id
      var formData = this.getFormData(item)
      var name = this.getName(item)
      // POST url
      this.$http.post(url, formData).then(response => {
        // success callback
        var notice = 'Сотрудник ' + name + ' успешно сохранен'

        this.$refs.edit_form.show(false)
        this.refreshItem(item)
        this.showNotice('success', notice)
      }, response => {
        // error callback
        var notice = 'Ошибка сохранения сотрудника ' + name + '. Причина: ' + response.body.message
        this.showNotice('error', notice)
      });      
    },
    getName (item) {
      return [item.first_name, item.second_name, item.last_name].join(' ')
    },
    transformItem (item) {
      var title = this.getName(item)
      var bday = item.birthday.split('-').reverse().join('.')
      var subtitle = ['Дата рождения:', bday].join(' ')
      return {
                icon: 'person',
                iconClass: 'blue white--text',
                title: title,
                subtitle: subtitle,
                is_archive: item.is_archive,
                id: item.id,
              }
    },
    showNotice (status, message) {
      console.log('showNotice', status, message)
      this.$refs.snack.show(status, message)
    },
    refreshItem (item) {
      console.log('refreshItem', item)
      var ind = this.items.findIndex(x => x.id === item.id)
      if (ind === -1) {
        console.log('IndexError')
      } else {
        this.$set(this.items, ind, this.transformItem(item))
      }
    },
    appendItem (item) {
      console.log('appendItem', item)
      var new_item = this.transformItem(item)
      this.items.push(new_item)
    },
    popItem (item) {
      console.log('popItem', item)
      var ind = this.items.findIndex(x => x.id === item.id)
      if (ind === -1) {
        console.log('IndexError')
      } else {
        this.items.splice(ind, 1)
      }
    },
  },
  created: function () {
    // Fetch our array from an API
    console.log(this.$http.options.root)
    this.$http.get('person').then(response => {
        // success callback
        var data = response.body
        var arr = []
        var len = data.length
        for (var i = 0; i < len; i++) {
            var item = data[i]
            var new_item = this.transformItem(item)
            arr.push(new_item)
        }        
        this.items = arr
    }, response => {
        // error callback
    })            
  },

}
</script>

<style>

</style>

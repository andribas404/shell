<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>

      <v-list two-line v-if="items.length">
        <ListItem
          v-for="item in items"
          :key="item.id"
          :item="item"
          @edit="editItem"
          @archive="archiveItem"
        />
      </v-list>
      <p v-else>
        Список сотрудников пуст.
      </p>

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
    </v-layout>
  </v-container>
</template>

<script>
import ListItem from './ListItem'
import PersonForm from './PersonForm'

export default {
  components: {
    ListItem, PersonForm
  },
  data: () => ({
    items: [],
  }),
  methods: {
		addItem () {
      console.log('add')
      this.$refs.add_form.show()
    },
    editItem (id) {
      console.log('edit', id)
      this.$refs.edit_form.set(id)
      this.$refs.edit_form.show()
    },
    removeItem (id) {
      console.log('remove', id)
    },
    archiveItem (id) {
      console.log('archive', id)
    },
    createItem (item) {
      console.log('createItem', item)
    },
    updateItem (item) {
      console.log('updateItem', item)
    },
  },
  created: function () {
    // Alias the component instance as `vm`, so that we  
    // can access it inside the promise function
    var vm = this
    // Fetch our array of dpts from an API
    this.$http.get('person').then(response => {
        // success callback
        var data = response.body
        var arr = []
        var len = data.length
        for (var i = 0; i < len; i++) {
            var item = data[i]
            var title = [item.first_name, item.second_name, item.last_name].join(' ')
            var bday = item.birthday.split('-').reverse().join('.')
            var subtitle = ['Дата рождения:', bday].join(' ')
            arr.push({
                icon: 'person',
                iconClass: 'blue white--text',
                title: title,
                subtitle: subtitle,
                id: data[i].id,
            })
        }        
        vm.items = arr
    }, response => {
        // error callback
    })            
  },

}
</script>

<style>

</style>

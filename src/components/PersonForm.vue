<template>
<v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
    <v-card>
        <v-toolbar dark color="blue darken-3" v-if="edit_mode">
        <v-btn icon dark @click="close">
            <v-icon>close</v-icon>
        </v-btn>
        <v-toolbar-title>Редактирование сотрудника</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
            <v-btn dark flat @click="$emit('update', item)">Сохранить</v-btn>
        </v-toolbar-items>
        </v-toolbar>

        <v-toolbar dark color="blue darken-3" v-else>
        <v-btn icon dark @click="close">
            <v-icon>close</v-icon>
        </v-btn>
        <v-toolbar-title>Добавление сотрудника</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
            <v-btn dark flat @click="$emit('create', item)">Создать</v-btn>
        </v-toolbar-items>
        </v-toolbar>

        <v-form v-model="valid">
        <v-container grid-list-md text-xs-center>
            <v-layout row wrap>
            <v-flex xs12 md4>
                <v-text-field
                v-model="item.first_name"
                :rules="fieldRules"
                label="Имя"
                required
                ></v-text-field>
            </v-flex>
    
            <v-flex xs12 md4>
                <v-text-field
                v-model="item.second_name"
                :rules="fieldRules"
                label="Отчество"
                required
                ></v-text-field>
            </v-flex>

            <v-flex xs12 md4>
                <v-text-field
                v-model="item.last_name"
                :rules="fieldRules"
                label="Фамилия"
                required
                ></v-text-field>
            </v-flex>

            <v-flex xs12 md4>
                <v-select
                    v-model="item.sex"
                    :items="sex_items"
                    :rules="fieldRules"
                    label="Пол"
                    required
                ></v-select>
            </v-flex>

            <v-flex xs12 md4>
                <v-text-field
                    v-model="item.birthday"
                    :rules="fieldRules"
                    mask="##.##.####"
                    label="Дата рождения"
                    required
                ></v-text-field>
            </v-flex>

            <v-flex xs12 md4>
                <v-select
                    v-model="item.dpt"
                    :items="dpt_items"
                    :rules="fieldRules"
                    label="Отдел"
                    required
                ></v-select>
            </v-flex>

            <v-flex xs12 md4>
                <v-text-field
                v-model="item.position"
                :rules="fieldRules"
                label="Должность"
                required
                ></v-text-field>
            </v-flex>

            <v-flex xs12 md4>
                <v-checkbox
                    v-model="item.is_archive"
                    label="В архиве"
                ></v-checkbox>
            </v-flex>
    
            <v-flex xs12 md4 v-if="edit_mode">
                <v-btn dark color="red" @click="confirm">
                    <v-icon>delete</v-icon> Удалить
                </v-btn>
            </v-flex>

            </v-layout>
        </v-container>
        </v-form>

    </v-card>
      <Confirmation
        :dialog="confirm_dialog"
        @confirm="confirmed"
        ref="confirm"/>

</v-dialog>

</template>

<script>
  import Confirmation from './Confirmation'

  export default {
    components: {
        Confirmation
    },
    props: {
        edit_mode: {
            type: Boolean,
        },
    },
    data: () => ({
    confirm_dialog: false,
    dialog: false,
    valid: false,
    item: {
        first_name: '',
        second_name: '',
        last_name: '',
        sex: null,
        birthday: '',
        dpt: null,
        position: '',
        is_archive: false,
    },
    // TODO: CSRF, version, id - all hidden
    fieldRules: [
      v => !!v || 'Обязательное поле',
    ],
    sex_items: [
        {text: 'Мужской', value: 'М'},
        {text: 'Женский', value: 'Ж'},
    ],
    dpt_items: [],
    }),
    methods: {
        set (id) {
            var url = 'person/' + id
            this.$http.get(url).then(response => {
                // success callback
                var data = response.body
                this.item = data
                this.item.dpt = data.dpt.id
                this.item.birthday = data.birthday.split('-').reverse().join('.')
            }, response => {
                // error callback
            })
        },
        show (dialog=true) {
          this.dialog = dialog
        },
        close () {
          this.dialog = false
        },
        confirm () {
          this.$refs.confirm.show()
        },
        confirmed () {
          this.$refs.confirm.show(false)
          this.$emit('remove', this.item)
        },
    },
    created: function () {
        this.$http.get('dpt').then(response => {
            // success callback
            var data = response.body
            var arr = []
            var len = data.length
            for (var i = 0; i < len; i++) {
                arr.push({
                    text: data[i].name,
                    value: data[i].id,
                })
            }        
            this.dpt_items = arr
        }, response => {
            // error callback
        })            
    },
  }
</script>

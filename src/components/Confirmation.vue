<template>
  <v-layout
    row
    justify-center
  >
    <v-dialog
      v-model="dialog"
      persistent
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">
          Подтверждение
        </v-card-title>
        <v-card-text>{{ text }}</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="green darken-1"
            flat
            @click="dialog = false"
          >
            Отмена
          </v-btn>
          <v-btn
            color="green darken-1"
            flat
            @click="$emit('confirm')"
          >
            Удалить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
  export default {
    data () {
      return {
        dialog: false,
        confirmed: false,
        text: 'Вы точно хотите удалить сотрудника?',
      }
    },
    methods: {
        show (dialog=true) {
            this.dialog = dialog
        },
    },
  }
</script>

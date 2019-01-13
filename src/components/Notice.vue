<template>
    <v-snackbar
      v-model="snackbar"
      top
      multi-line
      :timeout="3000"
    >
      {{ text }}
      <v-btn
        color="pink"
        flat
        @click="snackbar = false"
      >
        Закрыть
      </v-btn>
    </v-snackbar>
</template>

<script>
  export default {
    data () {
      return {
        snackbar: false,
        text: '',
        status: '',
      }
    },
    methods: {
        show (status, message) {
            this.status = status
            this.text = message
            this.snackbar = true
        },
    },
  }
</script>

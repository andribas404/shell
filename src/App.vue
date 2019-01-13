<template>
  <v-app>
    <v-layout row>
      <v-toolbar color="blue darken-3" dark app fixed>
        <v-toolbar-side-icon></v-toolbar-side-icon>
        <v-toolbar-title style="width: 300px" class="ml-0 pl-3">
          <span class="hidden-sm-and-down">Система учёта персонала</span>
        </v-toolbar-title>
      <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>notifications_none</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>widgets</v-icon>
        </v-btn>
        <v-btn icon href="https://github.com/andribas404/shell" target="_blank">
          <img height="32" width="32" src="/github.svg" />
        </v-btn>
      </v-toolbar>

      <v-content>
        <PersonsList/>
      </v-content>
    </v-layout>
  </v-app>
</template>

<script>
import PersonsList from './components/PersonsList'

export default {
  name: 'App',
  components: {
    PersonsList
  },
  data () {
    return {
      //
    }
  }
}
</script>

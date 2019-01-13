import Vue from 'vue'
import VueResource from 'vue-resource'

import './plugins/vuetify'
import App from './App.vue'

import { apiHost } from './config'

Vue.use(VueResource)
Vue.http.options.root = apiHost

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')

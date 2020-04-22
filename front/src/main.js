import Vue from 'vue';
import App from './App.vue';
import routes from './routes';
import VueRouter from 'vue-router';

Vue.config.productionTip = false

Vue.use(VueRouter)

new Vue({
  router: new VueRouter({ routes }),
  render: h => h(App),
}).$mount('#app')

import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import 'vuetify/src/stylus/app.styl'

Vue.use(Vuetify, {
  iconfont: 'md',
  theme: {
    primary: '#9C27B0',
    sucess: '#3cd1c2',
    info: '#ffaa2c',
    error: '#f83e70',
    background: '#EFF1EC'
  }
})

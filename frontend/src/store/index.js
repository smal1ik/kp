import Vue from 'vue'
import Vuex from 'vuex'
import { createApp } from 'vue'
import { createStore } from 'vuex'
import router from './../router'

//console.log(Vue)
//Vue.use(Vuex)

const store = createStore({
//const store = new Vuex.Store({
    state:{
        backendUrl: 'http://127.0.0.1:8000/api',
        status: '',
        token: localStorage.getItem('access_token') || '',
        user : {},
        isAuth: false,
    },
    mutations:{  
        refreshStateAuth (state) {
            // console.log('refresh auth in store')
            state.isAuth = !!state.token
            // console.log(state.isAuth)
        },
        setStateAuth (state, auth) {
            // console.log('set auth in store')
            state.isAuth = !!auth
            // console.log(state.isAuth)
        },
        logout (state) {
            localStorage.removeItem('access_token')      
            localStorage.removeItem('tmp_username') 
            state.isAuth = false
            router.push('/')

        },
        /*
        auth_request(state){
            state.status = 'loading'
        },
        auth_success(state, token, user){
            state.status = 'success'
            state.token = token
            state.user = user
        },
        auth_error(state){
            state.status = 'error'
        },
        logout(state){
            state.status = ''
            state.token = ''
      },//*/
    },
    actions:{
        /*
        login({commit}, user){
            return new Promise((resolve, reject) => {
              commit('auth_request')
              axios({url: `${state.backendUrl}/api/auth/jwt/create`, data: user, method: 'POST' })
              .then(resp => {
                //const token = resp.data.token
                const token = resp.data.access
                const refresh = resp.data.refresh
                //const user = resp.data.user
                localStorage.setItem('token', token)
                axios.defaults.headers.common['Authorization'] = token
                commit('auth_success', token, user)
                resolve(resp)
              })
              .catch(err => {
                commit('auth_error')
                localStorage.removeItem('token')
                reject(err)
              })
            })
          },
          logout({commit}){
            return new Promise((resolve, reject) => {
              commit('logout')
              localStorage.removeItem('token')
              delete axios.defaults.headers.common['Authorization']
              resolve()
            })
           },//*/
    },
    modules:{},
    getters:{
        /*
        getServerUrl(state){
            return state.backendUrl
        },//*/
        getUser: state=> state.user,
        getServerUrl: state => state.backendUrl,
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status,
        getAuth: state => state.isAuth,
    }
})




export default store
import axios from "axios"
import router from './../router'
import store from './../store'

        
const api = axios.create();
//start request
api.interceptors.request.use(config =>{
  if(localStorage.getItem('access_token')){
    config.headers.authorization = `JWT ${localStorage.getItem('access_token')}`    
  }
  return config
}, error =>{
})
//end request
api.interceptors.response.use(config =>{
  if(localStorage.getItem('access_token')){
    config.headers.authorization = `JWT ${localStorage.getItem('access_token')}`    
  }
  return config
}, error =>{
    if ( error.response.data.code === "token_not_valid"){
        return axios.post(`${store.getters.getServerUrl}/auth/jwt/refresh`, {        
            "refresh": localStorage.getItem('refresh_token')            
        }).then(res =>{
            //refresh token response
            localStorage.setItem('access_token', res.data.access)

            error.config.authorization = `JWT ${localStorage.getItem('access_token')}`
            // REPEAT!
            return api.request(error.config)
        }).error(err => {
            console.log('Logout - токен истёк.')            
            store.commit('logout') 
        })
    }
//   if(error.response.status === 401){            
//     router.push('/login')
//   }
})

export default api
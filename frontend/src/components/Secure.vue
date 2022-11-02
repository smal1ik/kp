<template>
    <div>
        <h2>Личный кабинет</h2>

        {{localStorage.getItem('tmp_username')}}

    </div>
</template>


<script>
import API from '../api/api'
export default {
  name: 'Secure',
  //props:,
  data(){
    return{
      secure_data: "",
      roles: [],
      localStorage
    }
  },
  components:{},
  created(){ 
      console.log('secure page')
      this.getSecure()
      this.getRoles()
      this.getServices()
  },
  methods:{    
      getSecure(){
        API.get(`${this.$store.getters.getServerUrl}/test`)
        .then( res => {
            console.log('response secure')
            console.log(res)
            console.log(localStorage.getItem('tmp_username'))
            this.secure_data = res.data.key
            //localStorage.setItem('access_token', res.data.access)
        })
        .catch(function (error) {
            console.log('error')
            console.log(error)
        })
      },
       getRoles(){
        API.get(`${this.$store.getters.getServerUrl}/get_roles`)
        .then( res => {
            console.log('response roles')
            console.log(res.data)
            this.roles = res.data.roles
            //localStorage.setItem('access_token', res.data.access)
        })
        .catch(function (error) {
            console.log('error')
            console.log(error)
        })
      },
       getServices(){
        API.get(`${this.$store.getters.getServerUrl}/service/for_me`)
        .then( res => {
            console.log('response services')
            console.log(res.data)
            this.services = res.data
            //localStorage.setItem('access_token', res.data.access)
        })
        .catch(function (error) {
            console.log('error')
            console.log(error)
        })
      },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

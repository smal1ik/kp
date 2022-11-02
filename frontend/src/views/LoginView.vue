<template>
  <div>

    <!-- <form class="login" @submit.prevent="login">
     <h1>Sign in</h1>
     <label>Login</label>
     <input required v-model="username" type="text" placeholder="username"/>
     <label>Password</label>
     <input required v-model="password" type="password" placeholder="password"/>
     <hr/>
     <button @click.prevent="login" type="submit">Login</button>
   </form> -->

   <v-card>
      <v-card-header>
        <v-card-header-text class="ma-4">
          <v-card-title color="white">Вход</v-card-title>

          <!-- <v-card-subtitle>
            <span class="mr-1">Используйте логин пароль</span>              
          </v-card-subtitle> -->
        </v-card-header-text> 
      </v-card-header>

      <v-container>
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
        @submit.prevent="login"
      >

        <v-text-field
          v-model="username"
          
          :rules="nameRules"
          label="Логин"
          variant="outlined"
          required
        ></v-text-field>

         <v-text-field
            v-model="password"
            name="input-10-1"
            label="Пароль"
            hint="Минимальное количество символов"          
            type="password"      
            variant="outlined"     
          ></v-text-field>
        <v-container 
            align="center">
            <v-btn 
            @click.prevent="login"
            type="submit" 
            color="primary"
          >
            Войти
          </v-btn>
        </v-container>


      </v-form>
      </v-container>

      <v-divider></v-divider>

      <v-card-actions class="justify-center">
        <v-btn @click="toRegister">Регистрация</v-btn>
        <v-btn @click="remindPassword" >Напомнить пароль</v-btn>
      </v-card-actions>
    </v-card>
    
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'Login',
  props: {
  },
  data(){
    return{
        user: {},
        username: "",
        password: "",
        valid: true,
        name: '',
        nameRules: [
          v => !!v || 'Name is required',
          v => (v && v.length <= 10) || 'Name must be less than 10 characters',
        ],
        email: '',
        emailRules: [
          v => !!v || 'E-mail is required',
          v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
        ],
    }
  },
  components:{},
  created(){
    console.log('created login')
    //console.log(this.$store.state.backendUrl)//getters.getServerUrl)
    //this.loadListSettings()
  },
  methods:{   
    toRegister(){
      console.log('register')
      this.$router.push('/reg/new/')
    },
    remindPassword(){
      console.log('remind password')
      
      this.$router.push('/reg/remind/')
    },
    // validate () {
    //   this.$refs.form.validate()
    // },
    // reset () {
    //   this.$refs.form.reset()
    // },
    // resetValidation () {
    //   this.$refs.form.resetValidation()
    // },
    login: function () {
      let username = this.username
      let password = this.password
      // console.log('url')
      // console.log(`${this.$store.getters.getServerUrl}/auth/jwt/create`)
      axios.post(`${this.$store.getters.getServerUrl}/auth/jwt/create`,{username: this.username, password: this.password})
      .then( res => {
          localStorage.setItem('access_token', res.data.access)
          localStorage.setItem('refresh_token', res.data.refresh)
          localStorage.setItem('tmp_username', username)
          this.$store.commit('setStateAuth', true)
          // this.$forceUpdate();
          this.$router.push("/")

          
      })
      .catch(function (error) {
          console.log('error')
          console.log(error)
      })
      /*
      this.$store.dispatch('login', { login, password })
      .then(() => this.$router.push('/'))
      .catch(err => console.log(err))//*/
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

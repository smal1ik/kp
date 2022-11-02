<template>
<!-- class="fill-height" -->
  <v-app  :theme='_theme'>
    
    <v-app-bar color="primary">

      <!-- <template v-slot:prepend>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
      </template> -->

      <v-app-bar-title>
        <v-btn @click="toHome">  
        Корпоративный портал
        </v-btn>
      </v-app-bar-title>
       
        <v-spacer></v-spacer>
       
        <!-- <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn> -->

        <v-btn 
          v-if="isLoggedIn"
          @click="Logout"
        >
          Выйти
        </v-btn>
        <v-btn  
          v-else
          @click="Login"
        >
          Войти
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>

         <template v-slot:append>
          <v-switch  @change="changeTheme" />
        </template>

      <!-- <template v-slot:append>
        <v-btn @click="Login">Войти</v-btn>

        <v-switch  @change="changeTheme" />

        <v-btn icon="mdi-dots-vertical" @click="changeTheme"></v-btn>
      </template> -->
    </v-app-bar>
    
    <v-main class="app-main" > 
      <v-container>
        <v-row >
          <v-col              
            lg="8"
            offset-lg="2"
          >
         
             <router-view/>
           
          </v-col>
        </v-row>        
      </v-container>     
    </v-main>
    

     <!--
    <v-navigation-drawer color="green-darken-2" permanent position="right"></v-navigation-drawer>
    <v-navigation-drawer color="blue-darken-2" temporary></v-navigation-drawer>


    <v-app-bar position="bottom" height="20" color="grey-lighten-2" elevation="0">
      подвал
    </v-app-bar> 
    
    class="grow d-flex flex-column flex-nowrap">
        <v-row no-gutters class="grow">
    -->
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({    
    _theme: 'light',
    isLoggedIn: false,
    _watch: undefined,
  }),
  //  computed: {
  //   isLoggedIn() {
  //     return this.$store.getters.isLoggedIn
  //   }
  // },
  watch: {
    // whenever question changes, this function will run
    // isLoggedIn() {
    //   if (this.isLoggedIn !== this.$store.getters.isLoggedIn) {
    //     this.isLoggedIn = this.$store.getters.isLoggedIn
    //   }
    // }
  },
  mounted(){
    

    console.log('mounted')
    this.$store.commit('refreshStateAuth')
    this.isLoggedIn = this.$store.state.isAuth
    console.log(this.isLoggedIn)

    console.log('watch')
    console.log(this.$store.state.isAuth)

    // this.$store.watch('isAuth', value => doThing(value), { immediate: true })

    var self = this
    this._watch = this.$store.watch(
      (state)=>{
        console.log('init watch')
        console.log(state)
        return state.isAuth//this.$store.state.isAuth // could also put a Getter here
      },
      (newValue, oldValue)=>{
        //something changed do something
        console.log('Changed!==============')
        console.log(oldValue)
        console.log(newValue)
        self.isLoggedIn = self.$store.state.isAuth
      },//Optional Deep if you need it
      {
        deep: true
      }
    )
    console.log(this.$store)
  }, 
   methods:{   
    //   updateThis(){
    //     console.log('manual update')
            
    //     this.$store.commit('setStateAuth', !this.isLoggedIn) 
    //     console.log(this.isLoggedIn)
    //     console.log(this.$store.getters.getAuth)
    //     this.isLoggedIn = this.$store.getters.getAuth
    //  },  
    toHome(){
      this.$router.push("/")
    },
    changeTheme(event){
    
      if(event.target._modelValue){
        this._theme = 'dark'
      } else{
        this._theme = 'light'
      }
    },
    Login(){
      this.$router.push('/login')
    },
    Logout(){
      // console.log('logout')
      /*Рабочий код! Переместить во VUEX
      localStorage.removeItem('access_token')
      localStorage.removeItem('tmp_username')
      this.$store.commit('setStateAuth', false)
      this.$router.push('/')
      //*/
      // вариант через VUEX
      this.$store.commit('logout') 
    },
   }
}
</script>

<style>
html,
body {
	height: 100%;
}

#app{
  height: 100%;
  /* position:relative;
  height:auto !important; 
  height: 100%; */
  /* min-height: 300px; */
  /* margin:0 auto; */
}
.v-application--wrap {
  min-height: unset;
}

.main-container {
  background-color:green;
	height: 100%;
  min-height: 100%;
	display: flex;
	flex-direction: column;
  padding: 10px;
}
.main-box {
  background-color:blue;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.main-box-flex{
  background-color:pink;
  flex: 1;
}

.scroll-y{
  overflow-y: auto;
}
.app-main{
  overflow-y: auto;
  height: 100%;
}

</style>

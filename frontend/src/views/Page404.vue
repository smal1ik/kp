<template>
    <v-card>
      <v-card-header>
        <v-avatar
          size="250"
          rounded="1"
        >
          <v-img
              src="/img/page404/cat404.jpg"
              cover
            ></v-img>
        </v-avatar>

        <v-card-header-text class="ma-4">
          <v-card-title color="white">Ошибка 404</v-card-title>

          <v-card-subtitle>
            <span class="mr-1">Искомая страница не найдена!</span>              
          </v-card-subtitle>
        </v-card-header-text> 
      </v-card-header>
     
      <v-divider></v-divider>

      <v-card-actions class="justify-center">         
        <v-btn @click="toHome">
          На главную страницу
        </v-btn>
      </v-card-actions>
    </v-card>
    
</template>


<script>
export default {
  name: 'Page404',
  data(){
    return{
    }
  },
  components:{},
  created(){ 
      console.log(this.$store)
      console.log(this.$store.getters.isLoggedIn)
      console.log(localStorage.getItem('token'))

      console.log(localStorage.getItem('token') || '')
  },
  methods:{
    toHome(){
      this.$router.push("/")
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

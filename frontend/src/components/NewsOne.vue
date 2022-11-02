<template>
  <div>
    
   
          <v-card class="my-4 pa-4" v-for="post in posts" :key="post.title">
            <v-card-header>
              <h1>{{post.title}}</h1>
            </v-card-header>
            
            <div v-if="post.short">
                {{post.shorttext}}
                <v-divider></v-divider>
                <v-card-actions>
                  
                  <v-btn @click="post.short = false">Читать дальше</v-btn>
                </v-card-actions>
            </div>
            <div v-else>
              {{post.text}}
            </div>
          
          </v-card>
      
  </div>
</template>


<script>
import API from '../api/api'
export default {
  name: 'News',
  props: ['id'],
  //props:,
  data(){
    return{
      posts: [],
    }
  },
  components:{},
  created(){ 
      console.log('news page')
      // this.getNews()
  },
  methods:{    
      getNews(){
        API.get(`${this.$store.getters.getServerUrl}/workers/all`)
        .then( res => {
            console.log('response staff')
            console.log(res.data)
            // this.staff = res.data
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

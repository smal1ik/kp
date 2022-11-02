<template>
  <div>
    
   
          <v-card class="my-4 pa-4" v-for="post in posts" :key="post.title">
            <v-card-header>
              <h1><p style="white-space: pre-line;">{{post.title}}</p></h1>
            </v-card-header>
            
            <div v-if="post.short">
              <p style="white-space: pre-line;">{{post.shorttext}}</p>
              <v-divider></v-divider>
              <v-card-actions>
                <v-btn @click="post.short = false">Читать дальше</v-btn>
                <v-btn v-if="editorNews" @click="this.$router.push(`/news/update/${post.id}`)">Редактировать</v-btn>
                <v-btn v-if="editorNews" @click="DelNews(post.id)">Удалить</v-btn>
              </v-card-actions>
            </div>

            <div v-else>
              <p style="white-space: pre-line;">{{post.text}}</p>
              <v-divider></v-divider>
              <v-card-actions>
                <v-btn @click="post.short = true">Скрыть</v-btn>
                <v-btn v-if="editorNews" @click="this.$router.push(`/news/update/${post.id}`)">Редактировать</v-btn>
                <v-btn v-if="editorNews" @click="DelNews(post.id)">Удалить</v-btn>
              </v-card-actions>
            </div>
          
          </v-card>

    <v-container v-if="editorNews"
        align="center">
      <v-btn @click="this.$router.push(`/news/addNews/`)" color="primary">
        Добавить новость
      </v-btn>
    </v-container>
      
  </div>
</template>


<script>
import API from '../api/api'

export default {
  name: 'News',
  //props:,
  data(){
    return{
      posts: [],
      editorNews: false,
    }
  },
  components:{},
  created(){ 
      console.log('news page')
      API.get(`${this.$store.getters.getServerUrl}/get_roles`).then(
          res => {
            //Нужно ли добавлять сюда админа или можно будет через админ панель назначить себе группу?
            this.editorNews = res.data.roles.includes('news_editor')
          }
      )
      this.getNews()
  },
  methods:{    
      getNews(){

        API.get(`${this.$store.getters.getServerUrl}/posts/all`)
        .then( res => {
            console.log('response staff')
            console.log(res.data)
            this.posts = res.data
        })
        .catch(function (error) {
            console.log('error')
            console.log(error)
        })
      },
    DelNews(id){

        API.delete(`${this.$store.getters.getServerUrl}/posts/delete/${id}`)
            .catch(function (error) {
          console.log('error')
              console.log(error)
      })
      for (let i = 0; i < this.posts.length ; i += 1) {
        if (this.posts[i].id == id) {
          this.posts.splice(i, 1)
        }
      }
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

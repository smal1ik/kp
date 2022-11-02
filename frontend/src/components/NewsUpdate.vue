<template>
  <div>


    <v-card class="my-4 pa-4">
      <v-card-header>
        <div>
          <span style="font-weight: bold">Tittle:</span>
          <p style="white-space: pre-line;">{{post.title}}</p>
        </div>
      </v-card-header>
      <v-card-header>
        <div>
          <span style="font-weight: bold">Short text:</span>
          <p style="white-space: pre-line;">{{post.shorttext}}</p>
        </div>
      </v-card-header>
      <v-card-header>
        <div>
          <span style="font-weight: bold">Text:</span>
          <p style="white-space: pre-line;">{{post.text}}</p>
        </div>
      </v-card-header>
    </v-card>

    <v-container>
      <v-form ref="form">
        <v-textarea
            v-model="post.title"
            label="Tittle"
            type="text"
            variant="outlined"
            :rules = "[rules.required]"
        >
        </v-textarea>

        <v-textarea
            v-model="post.shorttext"
            label="Short text"
            type="text"
            variant="outlined"
            :rules = "[rules.required]"
        >
        </v-textarea>

        <v-textarea
            v-model="post.text"
            label="Text"
            type="text"
            variant="outlined"
            :rules = "[rules.required]"
        >
        </v-textarea>

        <v-container
            align="center">
          <v-btn

              color="primary"
              @click="updateNews"
          >
            Изменить
          </v-btn>
        </v-container>

      </v-form>
    </v-container>

  </div>
</template>

<script>
import API from '../api/api'

export default {

  name: "NewsUpdate",

  data(){
    return{
      post: {},
      title: '',
      shorttext: '',
      text: '',
      short: true,
      rules: {
        required: value => !!value || 'Поле не может быть пустым.'
      },
    }
  },

  components:{},
  created(){
    console.log('update news page')
    API.get(`${this.$store.getters.getServerUrl}/get_roles`).then(
        res => {
          //Нужно ли добавлять сюда админа или можно будет через админ панель назначить себе группу?
          if (!res.data.roles.includes('news_editor')){
            this.$router.push(`/news/`)
          }
        })
    this.getNews()
  },

  methods:{
    getNews(){
      API.get(`${this.$store.getters.getServerUrl}/posts/${this.$route.params.id}`)
          .then( res => {
            this.post = res.data
          })
          .catch(function (error) {
            console.log('error')
            console.log(error)
          })

    },
    async updateNews() {
      if ((await this.$refs.form.validate()).valid) {
        API.put(
            `${this.$store.getters.getServerUrl}/posts/update/${this.$route.params.id}`,
            {title: this.post.title, shorttext: this.post.shorttext, text: this.post.text, short: this.post.short}
        ).catch(function (error) {
          console.log('error')
          console.log(error)
        })
        await this.$router.push(`/news/`)
      }
    }
  }


}
</script>

<style scoped>

</style>
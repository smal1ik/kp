<template>
  <div>


    <v-card class="my-4 pa-4">
      <v-card-header>
        <div>
          <span style="font-weight: bold">Tittle:</span>
          <p style="white-space: pre-line;">{{title}}</p>
        </div>
      </v-card-header>
      <v-card-header>
        <div>
          <span style="font-weight: bold">Short text:</span>
          <p style="white-space: pre-line;">{{shorttext}}</p>
        </div>
      </v-card-header>
      <v-card-header>
        <div>
          <span style="font-weight: bold">Text:</span>
          <p style="white-space: pre-line;">{{text}}</p>
        </div>
      </v-card-header>
    </v-card>

    <v-container>
      <v-form ref="form">
        <v-textarea
            v-model="title"
            label="Tittle"
            type="text"
            variant="outlined"
            :rules = "[rules.required]"
        >
        </v-textarea>

        <v-textarea
            v-model="shorttext"
            label="Short text"
            type="text"
            variant="outlined"
            :rules = "[rules.required]"
        >
        </v-textarea>

        <v-textarea
            v-model="text"
            label="Text"
            type="text"
            variant="outlined"
            :rules = "[rules.required]"
            required
        >
        </v-textarea>

        <v-container
            align="center">
          <v-btn

              color="primary"
              @click="AddNews"
          >
            Добавить
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
    console.log('Add news page')
    API.get(`${this.$store.getters.getServerUrl}/get_roles`).then(
        res => {
          //Нужно ли добавлять сюда админа или можно будет через админ панель назначить себе группу?
          if (!res.data.roles.includes('news_editor')){
            this.$router.push(`/news/`)
          }
        }
    )
  },

  methods:{
    async AddNews(){
      if ((await this.$refs.form.validate()).valid) {
        API.post(
            `${this.$store.getters.getServerUrl}/posts/new/`,
            {title: this.title, shorttext: this.shorttext, text: this.text, short: true}
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
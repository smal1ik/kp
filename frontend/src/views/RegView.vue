<template>
  <div>

    <h2>{{title}}</h2>
<!--    <p>Режим напоминания пароля: {{remindMode}}</p>-->
<!--    <p>Выбрать пользователя из списка в DV.       -->
<!--      Если у пользователя есть email, то выслать на него новый логин\пароль.-->
<!--      Если не нашли себя, позвоните Анне Гайдай и попросите добавить в справочник Docsvision.-->
<!--      </p>-->
<!--    <p>Начните вводить Имя или фамилию</p>-->

    <v-card>
      <v-card-header>
        <v-card-header-text class="ma-4">
          <v-card-title color="white"></v-card-title>
        </v-card-header-text>
      </v-card-header>

      <v-container>
        <v-form
            ref="form"

        >

          <v-text-field
              v-model="email"
              label="E-mail"
              variant="outlined"
              :rules="[rules.required, rules.email]"
          ></v-text-field>

          <p
              v-if="errors.length"
          >
            {{ errors }}
          </p>

          <v-container
              align="center">
            <v-btn
                type="submit"
                color="primary"
                @click="checkEmail"
            >
              Отправить
            </v-btn>
          </v-container>
        </v-form>
      </v-container>
    </v-card>

  </div>
</template>

<script>
import axios from "axios";
import API from '../api/api'
export default {
  name: 'Reg',
  props: {
    remindMode: undefined,
  },
  data(){
    return{
       title: '...',
       remind: false,
       email: null,
       errors: '',
       rules: {
         required: value => !!value || 'Поле не может быть пустым.',
         email: value => {
           const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
           return pattern.test(value) || 'Недействительная электронная почта'
         }
       },
    }
  },

  components:{},
  created(){
    console.log('remind mode');
    console.log(this.remindMode);
    if(this.remindMode === 'remind'){
      this.title = 'Восстановление пароля';
      this.remind = true;
    }else{      
      this.title = 'Регистрация нового пользователя';
      this.remind = false;
    }
  },
  methods:{
    checkEmail: function () {

      if (!this.errors.length) {
        if (this.remindMode === 'remind') {
           axios.post(`${this.$store.getters.getServerUrl}/auth/users/reset_password/`, {email: this.email})
              .then(res => {
                console.log(res)
              })
        }
        else {
          console.log('Тут должен быть запрос на регистрацию')

        }
        return true;
      }

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

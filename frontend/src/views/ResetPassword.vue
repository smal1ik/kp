<template>
  <div>

    <v-card>
      <v-card-header>
        <v-card-header-text class="ma-4">
          <v-card-title color="white">Восстановление пароля</v-card-title>
        </v-card-header-text>
      </v-card-header>

      <v-container>
        <v-form ref="form">
          <v-text-field
              v-model="password"
              :rules="[rules.required, rules.counter]"
              label="Пароль"
              type="password"
              variant="outlined"
              required
          >
          </v-text-field>

          <v-text-field
              v-model="password_confirm"
              :rules="[rules.required, rules.compare]"
              label="Повторите пароль"
              type="password"
              variant="outlined"
              required
          >
          </v-text-field>

          <v-container
              align="center">
            <v-btn

                color="primary"
                @click="resetPassword"
            >
              Изменить
            </v-btn>
          </v-container>

        </v-form>
      </v-container>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ResetPassword",
  data(){
    return{
      password: '',
      password_confirm: '',
      rules: {
        required: value => !!value || 'Поле не может быть пустым.',
        counter: value => value.length >= 8 || 'Длина пароля должны быть больше 8.',
        compare: value => value === this.password || 'Пароли не совпадают.'
      },
    }
  },
  methods: {
    async resetPassword() {

      if ((await this.$refs.form.validate()).valid){
          axios.post(
              `${this.$store.getters.getServerUrl}/auth/users/reset_password_confirm/`,
              {uid: this.$route.params.uid, token: this.$route.params.token, new_password: this.password}
          )
              .then(r => {
                console.log(r)
              })
          await this.$router.push('/login')
      }
    }
  }
}
</script>

<style scoped>

</style>
<template>
  <div>
    <v-card>
      <v-card-header>
         <div class="text-h6 mb-1">
          Главная страница
        </div>
      </v-card-header>

        <v-btn @click="this.$router.push('/staff')">Справочник сотрудников</v-btn>
        <v-btn v-if="isLoggedIn" @click="this.$router.push('/secure')">Профиль</v-btn>
        <v-btn v-else @click="this.$router.push('/login')">Логин</v-btn>
        <v-btn @click="this.$router.push('/news')">Новости</v-btn>
        <v-btn @click="this.$router.push('/staff')">Справочник</v-btn>

    </v-card>
  </div>
</template>

<script>

export default {
  name: 'Home',

  data: () => ({
    tmp: {},
    isLoggedIn: false,
    _watch: undefined,
  }),

  mounted() {
    this.$store.commit('refreshStateAuth')
    this.isLoggedIn = this.$store.state.isAuth

    var self = this
    this._watch = this.$store.watch(
        (state)=>{
          self.isLoggedIn = self.$store.state.isAuth
          return state.isAuth
        },

    )

  },

  methods: {

  }
}
</script>

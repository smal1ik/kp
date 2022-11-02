<template>
    <div>
        <h2>Single {{ this.id }}</h2>
        {{name}}
    </div>
</template>


<script>
export default {
  name: 'Single',
  props: ['id'],
  data(){
    return{
      setting:{},
      name: ""
    }
  },
  components:{},
  created(){ 
      console.log('single')

      console.log(this.id)
    this.loadSetting()
  },
  methods:{
      //*
   async loadSetting(){
        this.setting = await fetch(
        `${this.$store.getters.getServerUrl}/user_settings/${this.id}`
      ).then(response => response.json())
      console.log(this.setting)
      console.log(this.id)
      console.log(this.setting)
      this.name = this.setting.user.username
   }//*/
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

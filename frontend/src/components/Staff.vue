<template>
    <div>
        <h2>Справочник сотрудников</h2>
        <!-- single-line
          hide-details  -->
         <v-text-field
          v-model="search"
          append-icon="search"
          label="Поиск"          
        ></v-text-field>
        <v-table>
          <thead>
            <tr>
              <th class="text-left">ФИО</th>
              <th class="text-left">Телефон</th>
              <th class="text-left">Мобильный</th>
              <th class="text-left">Должность</th>
              <th class="text-left">Подразделение</th>
              <th class="text-left">Кабинет</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="item in filteredList"
              :key="item.id"              
              @click="openDialog(item)"
            >
              <td>{{ item.display_name }}</td>
              <td>{{ item.inner_phone }}</td>
              <td>{{ getPhone(item.mobile_phone) }}</td>
              <td>{{ item.post }}</td>
              <td>{{ item.department }}</td>
              <td>{{ item.room }}</td>

              <!-- <v-btn
                color="primary"
                @click="openDialog(item)"
              >
                ...
              </v-btn> -->
              
            </tr>
          </tbody>
        </v-table>

         <v-dialog
            v-model="dialog"
          >
            <v-card>
              <v-card-header>
                Карточка сотрудника
              </v-card-header>
              <v-card-text>
                <b>Фамилия:</b> {{this.selected.last_name}} <br>
                <b>Имя:</b> {{this.selected.first_name}}<br>
                <b>Отчество:</b> {{this.selected.middle_name}}<br>
                <b>Должность:</b> {{this.selected.post}}<br>
                <b>Подразделение:</b> {{this.selected.department}}<br>
                <b>Кабинет:</b> {{this.selected.room}}<br>
                <b>Внутренний телефон:</b> {{this.selected.inner_phone}}<br>
                <b>Внешний телефон:</b> {{this.selected.outer_phone}}<br>
                <b>Мобильный:</b> {{getPhone(this.selected.mobile_phone)}}<br>
                <b>Дата рождения:</b> {{this.selected.birth_date}}<br>
                <b>Почта:</b> {{ this.selected.mail}}<br>
                <b>Логин:</b> {{this.selected.account_name}}<br>

                <p v-if="this.selected.gender === 'Male'">
                  <b>Пол</b> мужской <br></p>
                <p v-else-if="this.selected.gender === 'Female'">
                  <b>Пол</b> женский <br></p>
                <p v-else></p>

              </v-card-text>
              <v-card-actions>
                <v-btn color="primary" block @click="dialog = false">Закрыть</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
    </div>
</template>


<script>
import API from '../api/api'
const re = /\s*(?:-|$)|(?:|$)\s*/
export default {
  name: 'Staff',
  //props:,
  data(){
    return{
      search: "",
      staff: [],
      dialog: false,
      selected: {},
    }
  },
  components:{},
  created(){ 
      console.log('staff page')
      this.getStaff()
      // this.getRoles()
      // this.getServices()
  },
   computed: {
    filteredList() {
      return this.staff.filter(item => {
        return (
            item.display_name.toLowerCase().includes(this.search.toLowerCase())
            || item.post.toLowerCase().includes(this.search.toLowerCase())
            || item.department.toLowerCase().includes(this.search.toLowerCase())
            || item.room.toLowerCase().includes(this.search.toLowerCase())
        )

      })
    },
   },
  methods:{

      getPhone(numberPhone) {
        //StringBuilder или Join?
        if(numberPhone) {
          String
          let str;
          str = numberPhone.split(re).join("");
          return "+7 (" + str.slice(1, 4) + ") " + str.slice(4, 7) + "-" + str.slice(7, 9) + "-" + str.slice(9);
        }
        return null;
      },
      openDialog(item){
        this.dialog = true
        this.selected = item
      },
      closeDialog(){
        this.dialog = false
        this.selected = {}
      },
      getStaff(){
        API.get(`${this.$store.getters.getServerUrl}/workers/all/`)
        .then( res => {
            console.log('response staff')
            console.log(res)
            this.staff = res.data
            
            // localStorage.setItem('access_token', res.data.access)
        })
        .catch(function (error) {
            console.log('error')
            console.log(error)
        })
      },
      /*
       getRoles(){
        API.get(`${this.$store.getters.getServerUrl}/get_roles`)
        .then( res => {
            console.log('response roles')
            console.log(res.data)
            this.roles = res.data.roles
            //localStorage.setItem('access_token', res.data.access)
        })
        .catch(function (error) {
            console.log('error')
            console.log(error)
        })
      },
       getServices(){
        API.get(`${this.$store.getters.getServerUrl}/service/for_me`)
        .then( res => {
            console.log('response services')
            console.log(res.data)
            this.services = res.data
            //localStorage.setItem('access_token', res.data.access)
        })
        .catch(function (error) {
            console.log('error')
            console.log(error)
        })
      },//*/
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

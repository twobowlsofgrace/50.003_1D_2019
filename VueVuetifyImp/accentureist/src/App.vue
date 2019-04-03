<template>
<!-- <div id='app'>
  <div id="nav">
    <router-link v-if="authenticated" to="/login" v-on:click.native="logout()" replace>Logout</router-link>
  </div> -->
    <v-app class="grey lighten-4">
      <v-content class="mx-4 mt-4">
        <router-view ></router-view> 
      </v-content>
    </v-app>
<!-- </div> -->
</template>

<script>


export default {
  name: 'App',
  data () {
    return {
      authenticated: false,
      mockAccount: {
        username: "testuser1",
        password: "Password123",
        // email: "test@test.com",
        // phonenumber: 62315009,
      }

    }
  },
  mounted(){
    if(!this.authenticated){
      this.$router.replace({name:'login'});
    }
  },
  methods:{
    setAuthenticated(status){
      this.authenticated = status;
    },
    logout(){
      this.authenticated = false;
    }
  }
}
</script>

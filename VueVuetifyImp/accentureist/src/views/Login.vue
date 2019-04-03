<template>
  <v-app id="login">
      <v-content>
        <v-container fluid fill-height>
          <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
              <v-card class="elevation-12">
                <v-toolbar dark color="black">
                  <v-toolbar-title class="text-uppercase white--text">
                    <span class='white--text'>Welcome To </span>
                    <span class="font-weight-light primary--text">Accenture</span>
                    <span>ist</span>
                  </v-toolbar-title>
                
                </v-toolbar>
                <v-card-text>
                  <v-form>
                    <v-text-field id="username" prepend-icon="person" name="login" label="Username" type="text" clearable>
                      <!-- <template v-slot:progress>
                        <v-progress-linear v-if="custom" :value="progress" :color="color" height="7"></v-progress-linear>
                      
                      </template> -->
                    </v-text-field>
                    <v-text-field id="password" prepend-icon="lock" name="password" label="Password" type="password" clearable></v-text-field>
                  </v-form>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <!-- <v-btn flat small class="transparent mb-2" to="./createuser">Create New User</v-btn> -->
                  <router-link class="nav-link my-3" to="/createuser"> Create New User</router-link>
                  <v-btn depressed class="primary mx-2 mb-2" to="./dashboard">Login</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-content>

  </v-app>
</template>



<script>
  export default {
    name: 'Login',
    data() {
      return {
        input: {
          username: "",
          password: ""
        },
      }
    },
    methods:{
      login(){
        Console.log(this.username)
        Console.log(this.password)
      }
    }
    // methods: {
    //   login() {
    //     if(this.input.username != "" && this.input.password != "") {
    //       if(this.input.username == this.$parent.mockAccount.username && this.input.password == this.$parent.mockAccount.password) {
    //         this.$emit("authenticated", true);
    //         this.$router.replace({ name: "ashboard" });
    //       } else {
    //         console.log("The username and / or password is incorrect");
    //       }
    //     } else {
    //       console.log("A username and password must be present");
    //     }
    //   }
    // }
  }
</script>


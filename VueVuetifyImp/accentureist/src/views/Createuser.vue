<template>
  <v-app class="createuser">
    <v-snackbar v-model="snackbar" :timeout="4000" top>
            <span>Account Sucessfully Created</span>
            <v-btn flat color="white" @click="snackbar=false">Close</v-btn>
    </v-snackbar>
      <v-content>
        <v-container fluid fill-height>
          <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
              <v-card class="elevation-12">
                <v-toolbar dark color="black">
                  <v-toolbar-title class="text-uppercase white--text">
                    <span class='white--text'>Sign Up With </span>
                    <span class="font-weight-light primary--text">Accenture</span>
                    <span>ist</span>
                  </v-toolbar-title>
                
                </v-toolbar>
                <v-card-text>
                  <v-form>
                    <v-container fluid>
                      <v-layout row wrap>
                        <v-text-field id="username" prepend-icon="person" name="login" label="Username" type="text" counter="25"></v-text-field>
                        <v-text-field id="password" prepend-icon="lock" name="password" label="Password" type="password"></v-text-field>
                        <v-text-field id="email" prepend-icon="email" name="email" label="Email" type="email"></v-text-field>
                        <v-text-field id="phonenumber" prepend-icon="phone" name="phonenumber" label="Contact Number" type="number"></v-text-field>
                      </v-layout>
                    </v-container>

                  </v-form>
                </v-card-text>
                <v-card-actions>
                  <v-btn flat to="/">Cancel</v-btn>
                  <v-spacer></v-spacer>
                  <v-btn depressed class="primary mx-2 mb-2" @click="submit" :loading="loading" to="/" @accountCreated="snackbar=true">Create Account</v-btn>
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
  data(){
    return{
      loading: false, //not implemented yet
      snackbar: false
    }
    //to create submit method to submit data to django
  },
  methods: {
    submit(){
      this.loading = true,
      console.log("account created"), /* eslint no-console:on*/
      this.loading = false,
      this.$emit('accountCreated') // eslint-disable-line no-console
      
    }
  }
}
</script>

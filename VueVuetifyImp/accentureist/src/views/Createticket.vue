<template>
    <div class="createuser">
      <Navbar />
        <v-card class="rounded-card">
          <v-card-title class="headline font-weight-regular black white--text">
            Create New Ticket
          </v-card-title>
          <v-card-text>
            <v-form class="px-3" ref="form">
              <v-text-field label="Title" v-model="ticket.title" prepend-icon="folder" box required background-color="#FAFAFA"></v-text-field>
              <v-textarea label="Ticket Desciption" v-model="ticket.content" prepend-icon='edit' box background-color="#FAFAFA"></v-textarea>
              <div id="checkboxes">
                <p class="grey--text--darken-1"> I would like to be contacted by: (Required) </p>
                <v-checkbox  label="Email" color="primary" value="email" v-model="ticket.contactmethod" hide-details></v-checkbox>
                <v-checkbox  label="Contact Number" color="primary" value="phone" v-model="ticket.contactmethod" hide-details></v-checkbox>
              </div>
              <v-spacer></v-spacer>
              <v-btn flat class="primary text--white mx-0 mt-3" to="./dashboarduser">Submit</v-btn>
              
            </v-form>
          </v-card-text>
        </v-card>
        <v-card class=" rounded-card mt-2 mb-4">
            <v-card-title class="headline font-weight-regular black white--text" >
              Preview Ticket
            </v-card-title>
            <v-card-text >
              <div class="px-3 mt-2">
                <p>Username: {{user.username}} </p>
                <p>Ticket Title: {{ ticket.title }}</p>
                <p>Description:</p>
                <p style="white-space: pre">{{ ticket.content }}</p>
                <p>Contact Method:</p>
                <ul>
                  <li v-for="(contactmethods,index) in ticket.contactmethod" :key="`contactmethods-${index}`">{{contactmethods}}</li>
                </ul>
                <span>Date: </span>
                {{ date.split("-").reverse().join("/")}}
              </div>
              
        
            </v-card-text>
    
            <v-card>
              <v-card-title class="font-weight-regular black blue-grey lighten-3 white--text">
                Notice
              </v-card-title>
              <v-card-text>
                <div class="px-1">
                  
                  <p> {{user.username}} will be contacted through this email: {{user.email}} or at contact number: {{user.phonenumber}} <br>
                  If any of the information is incorrect, please update your details at <router-link class="nav-link" to="/profile"> Profile</router-link> </p>
                </div>
              </v-card-text>
            </v-card>
        </v-card>
    
    </div>
    
</template>

<script>
import Navbar from '@/components/Navbar'
export default {
  components: {Navbar},
    data () {
        return {
            ticket: {
                title: '',
                content: '',
                contactmethod: []
              
            },
            date: new Date().toISOString().slice(0,10),
            user:{
              username: 'testuser1',
              email: 'test@test.com',
              phonenumber: '68795756'
            },
        }
    },
    methods: {
      
    }
}
</script>

<style>
.rounded-card{
    border-radius:10px;
}
</style>



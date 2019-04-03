<template>
  <div class="dashboarduser">
    <Navbar />
    <h1 class="heading grey--text">Tickets</h1>
    <v-container class="my-1">
      <v-layout row class="mb-3">
        <v-tooltip top>
          <v-btn small flat color="grey" @click="sortByStatus('status','date')" slot="activator">
            <v-icon left small>equalizer</v-icon>
            <span class="caption text lowercase">By Status</span>
          </v-btn>
          <span>Sort Tickets by Status</span>
        </v-tooltip>
        
        <v-tooltip top>
          <v-btn small flat color="grey" @click="sortByDate('date')" slot="activator">
          <v-icon left small>date_range</v-icon>
          <span class="caption text lowercase">By Date</span>
          </v-btn>
          <span>Sort Tickets by Date</span>
        </v-tooltip>
      </v-layout>

      <v-card class="pa-1" v-for="ticket in tickets" :key="ticket.title">
        <v-layout row wrap :class="`pa-3 ticket ${ticket.status}`">
          <v-flex xs12 md4>
            <div class="caption grey--text">Ticket Title</div>
            <div>{{ticket.title}}</div>
          </v-flex>
          <v-flex xs3 sm2 md2>
            <div class="caption grey--text">User</div>
            <div>{{ticket.username}}</div>
          </v-flex>
          <v-flex xs3 sm2 md2>
            <div class="caption grey--text">Date Posted</div>
            <div>{{ticket.date}}</div>
          </v-flex>
          <v-flex xs3 sm2 md1>
            <div class="caption grey--text">Attendent</div>
            <div>{{ticket.attendent}}</div>
          </v-flex>
          <v-flex >
            <div class="right">
                <v-chip small :class="`${ticket.status} white--text caption my-2`">{{ticket.status}}</v-chip>
              </div>
          </v-flex>
        </v-layout>
        <v-divider></v-divider>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar'
export default {
  components: {Navbar},
  data(){
    return{
      //To be retrieved from backend
      tickets:[
          {title: 'Insufficient Space',username:'testuser2', date:'01/15/19', attendent:'Admin1', status:'ongoing', content:'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!'},
          // {title: 'Unable to find function',username:'testuser5', date:'02/20/19',attendent:'Admin3', status:'resolved', content:'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!'},
          // {title: 'Invalid API Warning',username:'testuser3', date:'01/10/19',attendent:'Admin1', status:'unattended', content:'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!'},
          // {title: 'Account Information Request',username:'testuser1', date:'03/17/19',attendent:'Admin3', status:'unattended', content:'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!'},
          // {title: 'Time Out Request',username:'testuser4', date:'03/03/19',attendent:'Admin1', status:'ongoing', content:'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!'},
          {title: 'API missing call',username:'testuser2', date:'02/09/19',attendent:'Admin2', status:'unattended', content:'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!'},
      
    
      ]
    }
  },
  methods:{
    sortByStatus(status,date){
      this.tickets.sort((a,b) => (a[status]>b[status])||(a[date]<b[date]) ? -1:1)
    },
    sortByDate(prop){
      this.tickets.sort((a,b) => a[prop]<b[prop] ? -1:1)
    }
  }
  
}
</script>

<style>
.ticket.resolved{
  border-left: 4px solid #3CD1C2;
}
.ticket.ongoing{
  border-left: 4px solid orange
}
.ticket.unattended{
  border-left: 4px solid tomato;
}

.v-chip.resolved{
  background: #69F0AE;
}
.v-chip.ongoing{
  background: #ffaa2c;
}
.v-chip.unattended{
  background: #f83e70;
}

</style>


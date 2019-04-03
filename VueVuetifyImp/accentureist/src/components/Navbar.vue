<template>
    <nav>
        <v-toolbar app dark>
            <v-toolbar-side-icon @click="drawer=!drawer"></v-toolbar-side-icon>
            <v-toolbar-title class="text-uppercase white--text" > 
                <span class="font-weight-light purple--text">Accenture</span>
                <span>ist</span>

            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn flat color="grey" to="/">
                <span>Log Out</span>
                <v-icon> exit_to_app</v-icon>
            </v-btn>
        </v-toolbar>

        <v-navigation-drawer  v-model="drawer" app class="background">
            <v-list class="text-uppercase font-weight-light" dark>
                <v-list-tile v-for="link in links" :key="link.text" router :to="link.route" ripple>
                    <v-list-tile-action>
                        <v-icon class="primary--text">{{ link.icon }}</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title class="primary--text">{{ link.text }}</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
                <v-divider></v-divider>
                
            </v-list>
        </v-navigation-drawer>
        
    </nav>
</template>

<script>

export default {
    data (){
        return{
            drawer: false,
            links: [
                {icon: 'note_add', text: 'Create Ticket', route: '/createticket'},
                {icon: 'view_list', text: 'View Tickets', route: '/dashboard'},
                {icon: 'person', text: 'Profile', route: '/profile'},
            ],

        }
    }
}
</script>
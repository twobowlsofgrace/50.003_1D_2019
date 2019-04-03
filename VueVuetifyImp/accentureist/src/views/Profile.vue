<template>
  <div class="profile">
    <Navbar />
    <v-layout align-center justify-center>
      <v-flex sm12 md8>
        <v-card class="rounded-card">
          <v-card-title class="headline font-weight-regular black white--text">Profile</v-card-title>
          <v-card-text v-for="details in user" :key="details.username">
            <v-text-field :value="details.username" label="Username" box readonly prepend-icon="person" background-color="#FAFAFA"></v-text-field>
            <v-text-field :value="details.password" label="Password" box readonly prepend-icon="lock" :type="show3 ? 'text' : 'password'" background-color="#FAFAFA" ></v-text-field>
            <v-text-field
              v-model="modelemail"
              :hint="!isEditingEmail ? 'Click the icon to edit' : 'Click the icon to save'"
              :readonly="!isEditingEmail"
              :label="`${isEditingEmail ? '': details.email}`"
              persistent-hint
              prepend-icon="email"
              box
              background-color="#FAFAFA"
            >
              <template v-slot:append-outer>
                <v-slide-x-reverse-transition
                  mode="out-in"
                >
                  <v-icon
                    :key="`icon-${isEditingEmail}`"
                    :color="isEditingEmail ? 'success' : 'primary'"
                    @click="isEditingEmail = !isEditingEmail"
                    v-text="isEditingEmail ? 'check_circle' : 'edit'"
                  ></v-icon>
                </v-slide-x-reverse-transition>
              </template>
            </v-text-field>

            <v-text-field
              v-model="model"
              :hint="!isEditing ? 'Click the icon to edit' : 'Click the icon to save'"
              :readonly="!isEditing"
              :label="`${isEditing ? '': details.phonenumber}`"
              persistent-hint
              prepend-icon="phone"
              box
              background-color="#FAFAFA"
            >
              <template v-slot:append-outer>
                <v-slide-x-reverse-transition
                  mode="out-in"
                >
                  <v-icon
                    :key="`icon-${isEditing}`"
                    :color="isEditing ? 'success' : 'primary'"
                    @click="isEditing = !isEditing"
                    v-text="isEditing ? 'check_circle' : 'edit'"
                  ></v-icon>
                </v-slide-x-reverse-transition>
              </template>
            </v-text-field>

          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar'
  export default {
    components: {Navbar},
    data () {
      return {
        isEditingEmail: false,
        isEditing: false,
        model: null,
        modelemail: null,
        user: [
        { username: "testuser2", password: "Password123", email:"test@test.com", phonenumber:"62195009", isadmin:"No" }
      ]
      }
    }
  }
</script>


<style>
.rounded-card{
    border-radius:10px;
}
</style>
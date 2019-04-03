<template>
  <v-dialog max-width="600px">
    <v-btn flat fab small slot="activator" class="grey lighten-4">
        <v-icon>message</v-icon>
    </v-btn>
    <v-card>
      <v-card-title>
        <h2>Add a New Project</h2>
      </v-card-title>
      <v-card-text>
          <v-textarea></v-textarea>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data() {
    return {
    }
  }
}
</script>
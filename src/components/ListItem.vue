<template>
    <v-list-tile avatar @click="$emit('edit', item.id)">
        <v-list-tile-avatar>
            <v-icon :class="[item.iconClass]">{{ item.icon }}</v-icon>
        </v-list-tile-avatar>
        <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
            <v-list-tile-sub-title>{{ item.subtitle }}</v-list-tile-sub-title>
        </v-list-tile-content>
        <v-list-tile-action>
            <v-btn icon v-on:click.stop="$emit('archive', item.id)">
                <v-icon
                v-if="item.is_archive"
                color="grey lighten-1"
                >
                star_border
                </v-icon>
                <v-icon
                v-else
                color="yellow darken-2"
                >
                star
                </v-icon>            
            </v-btn>
        </v-list-tile-action>
    </v-list-tile>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      required: true
    }
  }
}
</script>

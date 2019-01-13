<template>
    <v-menu
      v-model="menu"
      :close-on-content-click="false"
      offset-y
    >
    <v-btn
        slot="activator"
        icon
      >
        <v-icon>widgets</v-icon>
    </v-btn>

      <v-card>
        <v-card-title primary-title>
            <v-layout column>
            <h3>Фильтр</h3>
            <v-radio-group v-model="choice">
                <v-radio
                    :key="0"
                    label="Только активные"
                    :value="0"
                ></v-radio>
                <v-radio
                    :key="1"
                    label="Только архив"
                    :value="1"
                ></v-radio>
                <v-radio
                    :key="2"
                    label="Все"
                    :value="2"
                ></v-radio>
            </v-radio-group>
            </v-layout>
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            flat
            @click="menu = false"
          >
            Отмена
          </v-btn>
          <v-btn
            color="primary"
            flat
            @click="menu = false"
          >
            Применить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-menu>
</template>

<script>
  export default {
    data: () => ({
      menu: false,
      choice: 1,
    })
  }
</script>

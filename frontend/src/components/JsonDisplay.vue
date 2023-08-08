<template>
  <div class="json-display">
    <div v-for="(value, key) in jsonData" :key="key">
      <h2>{{ key }}</h2>
      <template v-if="isObject(value)">
        <JsonDisplay :jsonData="value" />
      </template>
      <p v-else>{{ value }}</p>
    </div>
  </div>
</template>

<script>
import { ref, computed } from "vue";

export default {
  name: "JsonDisplay",
  props: {
    jsonData: Object,
  },
  setup(props) {
    const isObject = (value) => {
      return typeof value === "object" && value !== null;
    };

    return {
      isObject,
    };
  },
};
</script>

<style scoped>
.json-display {
  padding: 10px;
  border: 1px solid #ccc;
  background-color: #f5f5f5;
  overflow: auto;
}
h2 {
  margin-top: 10px;
}
</style>

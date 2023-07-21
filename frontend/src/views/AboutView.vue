<script setup lang="ts">
const tableData = [
  {
    name: "吴勉孜",
    telephone: "18983318285",
  },
  {
    name: "吴嘉桢",
    telephone: "空",
  },
];
</script>

<template>
  <el-text>开发者信息</el-text>
  <el-table :data="tableData" stripe style="width: 100%">
    <el-table-column prop="name" label="姓名" width="180"> </el-table-column>
    <el-table-column prop="telephone" label="电话"> </el-table-column>
  </el-table>
</template>

<style scoped></style>

<script setup lang="ts">
import { reactive, ref } from "vue";

let cvResult = ref(""); // TODO: 字符串变量，用于显示生成的CV
let cvJson = reactive({}); // TODO: json变量，用于在CV_JsonToText中调用
const CV_JsonToText = new Promise((resolve, reject) => {
  // TODO: 模块化转换函数
  // if (true) {
  //   resolve("生成成功的返回值");
  // } else {
  //   reject("生成失败的返回值");
  // }
});
</script>

<template>
  <div>
    <el-text>上传文件</el-text>
    <!--  TODO: 上传文件的按钮-->
  </div>
  <el-divider />
  <div>
    <el-text>此处替换为json文件内容</el-text>
  </div>
  <el-divider />
  <div>
    <!--  TODO: 下载文件-->
    <div>
      <el-text>{{ cvResult }}</el-text>
    </div>
    <el-button>下载简历</el-button>
  </div>
</template>

<style scoped></style>

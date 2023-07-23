<template>
  <div>
    <form @submit.prevent="submitForm">
      <label for="name">Name:</label>
      <input type="text" id="name" v-model="formData.name" required />

      <label for="email">Email:</label>
      <input type="email" id="email" v-model="formData.email" required />

      <label for="message">Message:</label>
      <textarea id="message" v-model="formData.message" required></textarea>

      <button type="submit">Submit</button>
    </form>

    <div>
      <el-text>{{ cvResult }}</el-text>
    </div>
    <el-button @click="downloadCV">下载简历</el-button>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from "vue";
import axios from "axios";

interface FormData {
  name: string;
  email: string;
  message: string;
}

const formData = reactive<FormData>({
  name: "",
  email: "",
  message: "",
});

const cvResult = ref<string>("");
const cvJson = reactive<Record<string, unknown>>({});

const submitForm = () => {
  // 将 formData 转换为 JSON 格式
  const jsonData = JSON.stringify(formData);

  // 使用 Axios 发送 JSON 数据到后端
  axios
    .post("/your-backend-api-url", jsonData, {
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response) => {
      // 处理响应结果
      console.log("Response from server:", response.data);
      cvResult.value = "生成成功的返回值";
    })
    .catch((error) => {
      // 处理错误
      console.error("Error sending data:", error);
      cvResult.value = "生成失败的返回值";
    });
};

const downloadCV = () => {
  // TODO: 下载简历的逻辑
};
</script>

<style scoped></style>

<template>
  <div>
    <el-divider />

    <el-row>
      <div>
        <el-col>
          <el-input
            v-model="question"
            type="textarea"
            style="width: 20rem"
            :autosize="{ minRows: 5, maxRows: 10 }"
            placeholder="请输入问题"
          ></el-input>
        </el-col>
        <el-col class="mv-1">
          <el-button @click="submitQue" :loading="loadingStatus"
            >提交</el-button
          >
          <el-button
            @click="
              () => {
                question = '';
              }
            "
            >清空</el-button
          >
        </el-col>
      </div>
    </el-row>
    <el-divider />
    <el-row>
      <div>
        <el-input
          v-model="queResult"
          type="textarea"
          style="width: 20rem"
          :autosize="{ minRows: 5, maxRows: 10 }"
          placeholder="生成的问题答案会显示在此处"
          readonly
        ></el-input>
      </div>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, Raw } from "vue";
let queResult = ref("");
let loadingStatus = ref(false);
let question = ref("");
const submitQue = () => {
  loadingStatus.value = true;
  fetch("http://localhost:5000/submit", {
    method: "POST",
    body: JSON.stringify({
      question: question.value,
    }),
    // mode: "no-cors",
    headers: {
      "Content-Type": "application/json",
      // "Content-Type": "text",
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
  })
    .then((res) => {
      if (res.ok) {
        res.json().then((data) => {
          console.log(data);
          queResult.value = data?.result;
        });
      }
    })
    .catch((e) => console.log(e))
    .finally(() => {
      loadingStatus.value = false;
    });
};
</script>

<style scoped></style>

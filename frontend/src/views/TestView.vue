<template>
  <div>
    <el-divider />

    <el-row style="display: flex; justify-content: space-evenly">
      <el-row>
        <el-input
          v-model="question"
          type="textarea"
          style="width: 40vw"
          :autosize="{ minRows: 20, maxRows: 100 }"
          placeholder="请输入问题"
        ></el-input>
      </el-row>
      <el-row>
        <el-divider
          direction="vertical"
          content-position="center"
          style="height: 100%"
        />
      </el-row>
      <el-row>
        <div>
          <el-input
            v-model.trim="queResult"
            type="textarea"
            style="width: 40vw"
            :autosize="{ minRows: 20, maxRows: 100 }"
            placeholder="生成的问题答案会显示在此处"
            readonly
          ></el-input>
        </div>
      </el-row>
    </el-row>
    <el-divider />
    <el-col class="mv-1" style="display: flex; justify-content: center">
      <el-button
        @click="submitQue"
        :loading="loadingStatus"
        :disabled="question.length == 0"
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
  <div class="m-3">
    <el-text style="font-weight: bold; font-size: large">简历预览</el-text>
    <JsonDisplay
      class="mt-3"
      v-if="jsonResult.hasContent"
      :json-data="jsonResult"
    ></JsonDisplay>
    <div v-else class="mv-1">
      <el-text>请先提交简历信息</el-text>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";
import { isJSON } from "@/tools/JsonTools";
import JsonDisplay from "@/components/JsonDisplay.vue";
let queResult = ref("");
let jsonResult = ref({ hasContent: false });
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
          let str: string = data.result;
          let str2 = str.substring(str.indexOf("{"), str.lastIndexOf("}") + 1);
          if (isJSON(str2)) {
            queResult.value = JSON.stringify(JSON.parse(str2), null, 4);
            jsonResult.value = JSON.parse(str2);
            jsonResult.value.hasContent = true;
            // console.log(jsonResult);
          } else {
            queResult.value = str;
            jsonResult.value = { hasContent: false };
          }
          console.log(queResult.value);
        });
      }
    })
    .catch((e) => {
      // FIXME: 异常JSON反馈
      console.log(e);
    })
    .finally(() => {
      loadingStatus.value = false;
    });
};
</script>

<style scoped></style>

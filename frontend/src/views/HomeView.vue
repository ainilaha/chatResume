<template>
  <div>
    <el-divider />

    <el-row>
      <div class="uploadDemo">
        <el-col>
          <el-input
            v-model="demo"
            type="textarea"
            style="width: 20rem"
            :autosize="{ minRows: 5, maxRows: 10 }"
            placeholder='请输入json格式，例如{"name":"LiHua","email":"lihua@my.com}'
          ></el-input>
        </el-col>
        <el-col class="mv-1">
          <el-upload
            class="upload-demo"
            ref="upload"
            accept=".json"
            action=""
            :on-change="changeDemoFile"
            :file-list="demoFileList"
            :auto-upload="false"
          >
            <template #trigger>
              <el-button size="small" type="primary">选取文件填充</el-button>
            </template>
            <span class="ml-1">
              <el-text>{{ message }}</el-text>
            </span>
          </el-upload>
        </el-col>
      </div>
    </el-row>
    <el-divider />
    <el-row>
      <div v-if="!isEmptyObj(cvResult)" ref="compToDownload">
        <json-display :json-data="cvResult"></json-display>
        <!--        <el-input-->
        <!--          v-model="cvResult"-->
        <!--          type="textarea"-->
        <!--          style="width: 20rem"-->
        <!--          :autosize="{ minRows: 5, maxRows: 10 }"-->
        <!--          placeholder="生成的简历会显示在此处"-->
        <!--          readonly-->
        <!--        ></el-input>-->
      </div>
    </el-row>
    <el-button @click="generateCV" class="mt-1">生成简历</el-button>
    <el-button @click="downloadCV" class="mt-1" :loading="loadingStatus"
      >下载简历</el-button
    >
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, Raw } from "vue";

import type { UploadInstance, UploadUserFile } from "element-plus";
import { ElNotification } from "element-plus";
import { isEmptyObj, isJSON } from "@/tools/JsonTools";
import JsonDisplay from "@/components/JsonDisplay.vue";
import { downloadPDF } from "@/tools/pdfTools";

const compToDownload = ref();
const loadingStatus = ref(false);
const upload = ref<UploadInstance>();

let demo = ref("");
let demoFileList = ref([] as UploadUserFile[]);
let message = ref("");

const changeDemoFile = (file: File | Raw<any>, demoFileList: void[]) => {
  if (demoFileList.length == 2) {
    //只保留最新的文件
    demoFileList.shift();
  }
  if (file.name.slice(-5) != ".json") {
    alert("只能读取json文件，请重新选择");
  } else {
    // console.log(file.raw);
    let fileReader = new FileReader();
    fileReader.onload = async (e) => {
      try {
        let document = JSON.parse(e.target?.result as string);
        console.log(document);
        demo.value = JSON.stringify(document);
        if (isJSON(demo.value)) {
          message.value = "满足json格式";
          ElNotification.success({
            title: "上传成功",
            offset: 100,
          });
        } else {
          message.value = "不满足json格式，请重新选择文件或修改文件";
          upload.value?.clearFiles();
          demo.value = "";
          ElNotification.error({
            title: "上传失败",
            message: "文件不是json格式",
            offset: 100,
          });
        }
      } catch (err) {
        console.log(err);
        upload.value?.clearFiles();
        message.value = "不满足json格式，请重新选择文件或修改文件";
        ElNotification.error({
          title: "上传失败",
          message: "文件不是json格式",
          offset: 100,
        });
        demo.value = "";
      }
    };
    fileReader.readAsText(file.raw);
  }
};

// interface FormData {
//   name: string;
//   email: string;
// }
// const formData = reactive<FormData>({
//   name: "",
//   email: "",
// });

let cvResult = reactive({});
// let cvJson = reactive({} as FormData);
let cvJson = reactive({});

// const submitForm = () => {
//   // 将 formData 转换为 JSON 格式
//   const jsonData = JSON.stringify(formData);

// 使用 Axios 发送 JSON 数据到后端
// axios
//   .post("/your-backend-api-url", jsonData, {
//     headers: {
//       "Content-Type": "application/json",
//     },
//   })
//   .then((response) => {
//     // 处理响应结果
//     console.log("Response from server:", response.data);
//     cvResult.value = "生成成功的返回值";
//   })
//   .catch((error) => {
//     // 处理错误
//     console.error("Error sending data:", error);
//     cvResult.value = "生成失败的返回值";
//   });
// };

const generateCV = () => {
  if (demo.value.length <= 0) {
    ElNotification.warning({
      title: "无法生成",
      message: "请先填写json信息",
      offset: 100,
    });
    return;
  }
  try {
    cvJson = JSON.parse(demo.value);
  } catch {
    ElNotification.error({
      title: "生成失败",
      message: "简历信息不是json格式",
      offset: 100,
    });
    return;
  }
  // cvResult = cvJson;
  for (let key in cvJson) {
    cvResult[key] = cvJson[key];
  }
  console.log(cvResult);
  // cvResult.hasContent = true;

  // if (!cvJson.value.name || !cvJson.value.email) {
  //   ElNotification.error({
  //     title: "生成失败",
  //     message: "简历信息不正确",
  //     offset: 100,
  //   });
  //   return;
  // }
  // cvResult.value = `我叫${cvJson.value.name}, 我的邮箱是${cvJson.value.email}`;
  // cvResult.value = `我叫${cvJson.name}, 我的邮箱是${cvJson.email}`;
  ElNotification.success({
    title: "生成成功",
    offset: 100,
  });
};

const downloadCV = () => {
  loadingStatus.value = true;
  downloadPDF(compToDownload.value).finally(() => {
    loadingStatus.value = false;
  });
};
</script>

<style scoped></style>

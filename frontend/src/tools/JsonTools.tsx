export const isJSON = (str: string) => {
  // 判断一个string是否是json类型，用于格式校验
  try {
    const obj = JSON.parse(str);
    return typeof obj == "object" && obj;
  } catch (e) {
    console.log("error：" + str + "!!!" + e);
    return false;
  }
};

// export const appendNode = (data) => {
//   const newChild = { id: id++, label: "testtest", children: [] };
//   if (!data.children) {
//     this.$set(data, "children", []);
//   }
//   data.children.push(newChild);
// };
// export const remove = (node, data) => {
//   const parent = node.parent;
//   const children = parent.data.children || parent.data;
//   const index = children.findIndex((d) => d.id === data.id);
//   children.splice(index, 1);
// };
//
// export const renderContent = (h, { node, data, store }) => {
//   return (
//     <span class="custom-tree-node">
//       <span>{node.label}</span>
//       <span>
//         <el-button size="mini" type="text" on-click={() => this.append(data)}>
//           Append
//         </el-button>
//         <el-button
//           size="mini"
//           type="text"
//           on-click={() => this.remove(node, data)}
//         >
//           Delete
//         </el-button>
//       </span>
//     </span>
//   );
// };

# onboxcreative.com 完整镜像（媒体已本地化）

这是 www.onboxcreative.com 的原版 Next.js 构建产物镜像（非重写版本），
包含原站的 HTML、CSS、JS chunk、字体和路由数据，渲染效果与原站逐像素一致，
动画与交互（GSAP 开场动画、页面过渡、客户端路由）完全相同。
所有图片和视频已下载到本地，不再依赖原站的 CDN。

## 本地运行

```bash
node server.mjs        # 默认端口 4173
node server.mjs 8080   # 指定端口
```

打开 http://localhost:4173

## 媒体文件位置（想换图/换视频改这里）

| 目录 | 内容 |
|---|---|
| `site/ext/sanity/images/7nifcbro/production/` | 全站所有图片（原 Sanity CMS 图片，文件名 = 内容哈希-尺寸.扩展名） |
| `site/ext/video/` | 全站所有视频，命名为 `<VimeoID>-<分辨率>.mp4`（如 `1174109130-2160p.mp4`） |
| `site/ext/vimeo-img/` | 视频封面图（poster），命名为 `<缩略图ID>.jpg` |

替换方法：**保持文件名不变**，用你的新文件覆盖旧文件即可，页面引用无需改动。
根目录的 `media-map.json` 记录了每个原始 CDN URL 对应的本地文件路径，
方便你对照"页面上这张图对应哪个文件"。

注意：站内引用不带宽高参数改写，同一文件会被不同分辨率的 srcset 引用，
替换时用尺寸相近的图即可，浏览器会自行缩放。

## 部署到 Vercel

仓库根目录已备好 `vercel.json` 和 `api/image.mjs`：

1. `git init && git add -A && git commit` 后 push 到 GitHub
2. Vercel 导入该仓库，Framework 选 **Other**，其余保持默认（`vercel.json`
   已指定静态目录为 `site/`，并把 `/_next/image` 图片请求重写到 `api/image.mjs`）
3. 部署即可，无需构建命令

仓库约 1.5GB（视频 850MB、图片约 590MB，单文件最大 31MB），低于 GitHub
单文件 100MB 限制，可以直接 push，首次 push 耗时较长属正常。

## 目录结构

- `site/` — 镜像站点（42 个页面 + `_next` 静态资源 + `ext/` 本地化媒体）
- `server.mjs` — 本地零依赖服务器（干净 URL + `/_next/image` 重定向）
- `api/image.mjs` — Vercel 上等价于 server.mjs 里 `/_next/image` 处理的函数
- `vercel.json` — Vercel 静态部署配置
- `media-map.json` — 原始 CDN URL → 本地文件 对照表

## 已知限制

1. **联系表单**：`/contact` 的表单提交依赖原站后端接口，不会真正发送。
2. **`/work/stocktwits`**：原站该 URL 本身是死循环重定向（原站也打不开），
   从 /work 列表页点进去（客户端路由）正常，本镜像行为一致。
3. **视频改为渐进式播放**：原站在线时用 Vimeo 自适应流（HLS），本地化后
   统一回退为渐进式 MP4（播放器自带的降级路径），画质为原站提供的最高档，
   观感无差别。
4. **一条无害的死链**：Vimeo ID 1056895104 的视频直链在 Vimeo 侧已失效
   （原站也是如此），但该媒体的 `mediaType` 是 image，页面实际渲染配图，
   这条 URL 永远不会被请求，故保留原样。
5. **控制台的 React 水合警告**：因为把 HLS 流地址置空改用本地 MP4，
   首次加载时控制台会出现 React #418/#423 水合警告，React 会自动回退
   客户端渲染，页面显示和视频播放不受影响，可忽略。
6. **这是编译产物，不是可维护源码**：改文案可直接编辑 HTML 和
   `site/_next/data/` 里的 JSON；要大改设计需另行重建可编辑的源码工程。

## 技术信息（原站）

- Next.js（Pages Router）+ React，部署于 Vercel
- CMS：Sanity（project id: 7nifcbro）；视频：Vimeo
- buildId: `NkaLovy8M3OdV54UztOF0`

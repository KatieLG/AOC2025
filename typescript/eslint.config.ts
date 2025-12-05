import tseslint from "typescript-eslint";
import { defineConfig } from "eslint/config";
import prettier from "eslint-config-prettier";

export default defineConfig(...tseslint.configs.recommended, prettier, {
  ignores: ["node_modules/"],
  rules: {
    "@typescript-eslint/explicit-function-return-type": "error",
  },
});

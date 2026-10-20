# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## Unreleased

<small>[Compare with latest](https://github_kamoyl/kamoyl/AWS_automation/compare/a523402bebf0b125623026594c32ddacfca6270a...HEAD)</small>

### Added

- Added buckets logging ([1653cec](https://github_kamoyl/kamoyl/AWS_automation/commit/1653cec4cebb239ffbd7c680bb5beb5def739739) by Kamil Czarnecki).
- Add scripts - init of a branch ([3e542eb](https://github_kamoyl/kamoyl/AWS_automation/commit/3e542eb04415c3fd59a628b767c3911976ca63d2) by Kamil Czarnecki).

### Changed

- Changelog ([11d6882](https://github_kamoyl/kamoyl/AWS_automation/commit/11d68826a252d3a39e14032af00807d2d1591737) by Kamil Czarnecki).
- Changed slack proxy parameters to array due to missunderstanding of dashes in variable ([0c34e9a](https://github_kamoyl/kamoyl/AWS_automation/commit/0c34e9a85e69e6ccea6b574585497db4e3141ace) by Kamil Czarnecki).

### Misc

- lots of updates ([b00f6c2](https://github_kamoyl/kamoyl/AWS_automation/commit/b00f6c2b292e116c102657a9639c7320533aa8d9) by Kamil Czarnecki).
- * lots of changes ([78251b2](https://github_kamoyl/kamoyl/AWS_automation/commit/78251b2ea9fcceb08d7f70808bbf16d45d7da543) by Kamil Czarnecki).
- Corrected key analysis ([2dbb2a4](https://github_kamoyl/kamoyl/AWS_automation/commit/2dbb2a42d235cf3c6985e1bd269edecf61098bc1) by Kamil Czarnecki).
- * correction of Lambda update, after AMI removal - provided properly: network ID, type of EC2 and region... ([fc64508](https://github_kamoyl/kamoyl/AWS_automation/commit/fc645081a967f662dd10710ab663985743aefd0c) by Kamil Czarnecki).
- * Changelog ([08bb177](https://github_kamoyl/kamoyl/AWS_automation/commit/08bb1775494db8725549c88f794fa997bde4e94c) by Kamil Czarnecki).
- * added removal of the oldest AMI - when there are more then 2 AMIs only ([0d5e1c7](https://github_kamoyl/kamoyl/AWS_automation/commit/0d5e1c7cd9f5263e991a168b46c947b2a88422e7) by Kamil Czarnecki).
- * added removing target ID from the EventRule if the actual target (for example Lambda function) doesn't exist ([61d2bc7](https://github_kamoyl/kamoyl/AWS_automation/commit/61d2bc790db0edd4fdb839173e5c7be433006413) by Kamil Czarnecki).
- * added check if SNS topic is encrypted ([c004217](https://github_kamoyl/kamoyl/AWS_automation/commit/c004217fa291c2576e2d80f28737b8e61a29cd5d) by Kamil Czarnecki).
- * updated changelog ([cdc3b0e](https://github_kamoyl/kamoyl/AWS_automation/commit/cdc3b0e75d4de36d24bfb5cc0aae5cf4f770a07e) by Kamil Czarnecki).
- * corrected cidr presentation or VPCs ([8443cba](https://github_kamoyl/kamoyl/AWS_automation/commit/8443cba5b3869221ee725537eef828b1588c1af4) by Kamil Czarnecki).
- * added collecting more then one VPC ([91363f2](https://github_kamoyl/kamoyl/AWS_automation/commit/91363f24bd21a91605f09f8a4b18dea445791de0) by Kamil Czarnecki).
- * added some constrains to check aws, az, and jq commands - as not needed except of those scripts ([e04395a](https://github_kamoyl/kamoyl/AWS_automation/commit/e04395a043205d58275e800b430f2bc3e5ce00f1) by Kamil Czarnecki).
- * checking aws version is ONLY when script starts with aws_ ([9aba3a6](https://github_kamoyl/kamoyl/AWS_automation/commit/9aba3a69015e8812151434e1fb7371379154cc0b) by Kamil Czarnecki).
- * changed place with counting runtime functions ([2546eff](https://github_kamoyl/kamoyl/AWS_automation/commit/2546efff01b59579adcf3ec788b3d1aab32cf072) by Kamil Czarnecki).
- * due to differernt crons I had to rewrite events and rules naming - without * and ? ([2c48cc5](https://github_kamoyl/kamoyl/AWS_automation/commit/2c48cc50e9c1f30c94fa668f6bee60164cd1a742) by Kamil Czarnecki).
- * added runtime as a funtion, to easily analaze where script needs optimization ([562c703](https://github_kamoyl/kamoyl/AWS_automation/commit/562c703a3f81ce2e5dc513e853461e281da0dd45) by Kamil Czarnecki).
- * added runtime function ([55aafed](https://github_kamoyl/kamoyl/AWS_automation/commit/55aafedee63e8c684fb13ef25cea1017b5bc2048) by Kamil Czarnecki).
- * Corrected/added permissions from lambda to events ([ab4c605](https://github_kamoyl/kamoyl/AWS_automation/commit/ab4c6059478161bf134a42b5ebf8f3a6ca680601) by Kamil Czarnecki).
- * lots of parallel run instead of linear... gained about 30% of time during run ([a3ecef4](https://github_kamoyl/kamoyl/AWS_automation/commit/a3ecef4ff44c153969f7187ed5148402aad98501) by Kamil Czarnecki).
- * corrected AMI creation ([d33f8f2](https://github_kamoyl/kamoyl/AWS_automation/commit/d33f8f2ddc981fcc5ecde018ae2064269054c3cb) by Kamil Czarnecki).
- * listing KMS keys ([10ee238](https://github_kamoyl/kamoyl/AWS_automation/commit/10ee238cefee2688e60b9993d642a4426953ea63) by Kamil Czarnecki).
- * small correction of notifications ([aa8cad6](https://github_kamoyl/kamoyl/AWS_automation/commit/aa8cad6c0dd5db856a9dfd3d956d240b30f66e8b) by Kamil Czarnecki).
- * corrected collecting roles and policies, and relations to them, due to one policy can be attached to many roles, and one role can have attached many polices, which were earlier not taken into consideration, and ... there was no isseu erlier ([f8bbb37](https://github_kamoyl/kamoyl/AWS_automation/commit/f8bbb37e0e4b04861caa7177662db727614f0045) by root).
- * corrected mounting buckets check ([61e59ce](https://github_kamoyl/kamoyl/AWS_automation/commit/61e59ce7c33b377919ffb4deadcb723bddfc8c50) by Kamil Czarnecki).
- * corrected empty space generating during terminal notifications ([7753fff](https://github_kamoyl/kamoyl/AWS_automation/commit/7753fff91e4f69dad54f8866e433582937ffdcef) by Kamil Czarnecki).
- * added slack notification function ([22dae21](https://github_kamoyl/kamoyl/AWS_automation/commit/22dae21dd09db946a7661152f9cfd354cd30dd63) by Kamil Czarnecki).
- * Added extra info about IFS ([9e6c331](https://github_kamoyl/kamoyl/AWS_automation/commit/9e6c331cac2ffcae5dcda0409a0f630f328d4997) by Kamil Czarnecki).
- * corrected retention time for logs for lambdas ([3057952](https://github_kamoyl/kamoyl/AWS_automation/commit/3057952637f340eaa08016bd3b0feff8c5951bf5) by Kamil Czarnecki).
- * added retention policy to logs - checking and applying ([b98e9db](https://github_kamoyl/kamoyl/AWS_automation/commit/b98e9db0dcb95e1c7b137db234e7d6eaef1de132) by Kamil Czarnecki).
- * slightly changed title of slack nofification ([12e7e3d](https://github_kamoyl/kamoyl/AWS_automation/commit/12e7e3d50a8294ef73ecb711d14a8cca109e229f) by Kamil Czarnecki).
- * changed completely collecting eventbridge rules and all targets of all rules ([6e90a1a](https://github_kamoyl/kamoyl/AWS_automation/commit/6e90a1ac1bc3178cca028f3e1d08e7140fe94107) by Kamil Czarnecki).
- * change cron to common schedule - so understands also rate ([11b2ec1](https://github_kamoyl/kamoyl/AWS_automation/commit/11b2ec1e3f44419d9073dccc6cd348e2100f550e) by Kamil Czarnecki).
- * updated Public IP entry ([6a895aa](https://github_kamoyl/kamoyl/AWS_automation/commit/6a895aa0fc717fd3d7d1425eb3dad30710ca98da) by Kamil Czarnecki).
- Update README.md ([b8324b9](https://github_kamoyl/kamoyl/AWS_automation/commit/b8324b94d9147e6fba7156daaf2fcd15d5134c5a) by Kamil Czarnecki).
- Updated README ([6ceb51a](https://github_kamoyl/kamoyl/AWS_automation/commit/6ceb51a224f27dfa52fe89a242fc283da84801e7) by Kamil Czarnecki).
- * lambda name has been changed to be used more then one - accordingly to destination scripts ([fa19656](https://github_kamoyl/kamoyl/AWS_automation/commit/fa19656036d98f5c1321ac1fca248ae4174aefb3) by Kamil Czarnecki).
- * slow change to separation error logs from output files ([38e0bae](https://github_kamoyl/kamoyl/AWS_automation/commit/38e0bae5adfa740423d791d13a9fd7402470404e) by Kamil Czarnecki).
- * added slack notification to deployment of lambda, target and event rule ([8754dd7](https://github_kamoyl/kamoyl/AWS_automation/commit/8754dd77482626a157744313502416945b9336c7) by Kamil Czarnecki).
- * separated some output files from error files when output is redirected ([39f9588](https://github_kamoyl/kamoyl/AWS_automation/commit/39f9588241bd96e1dc720a486767303fda22300b) by Kamil Czarnecki).
- Small notification change ([66c36ae](https://github_kamoyl/kamoyl/AWS_automation/commit/66c36ae7f65834fb5f1664925dbf2e33f687d3f1) by Kamil Czarnecki).
- * corrected issue with inapropriately checking subnets without tags ([c0078f1](https://github_kamoyl/kamoyl/AWS_automation/commit/c0078f134c69cbb83513fe3593fa6c38fd5bb7e5) by Kamil Czarnecki).
- few correction and few checkes to do smoothly through ([e9ee4a1](https://github_kamoyl/kamoyl/AWS_automation/commit/e9ee4a16a8487b20a73e2cf2d52e60680591b559) by Kamil Czarnecki).
- Lots of changes ([7d1cdd5](https://github_kamoyl/kamoyl/AWS_automation/commit/7d1cdd512198362868b5df01931c0ddb12b32cab) by Kamil Czarnecki).
-  * all scripts are prepared now to be run outside AWS instance, and from it either - it means that cleaning is safe (current instance will be untouched, so as policied, secure groups, etc), profile is taken properly frmo inside EC2 instance and from autiside ([3db6c43](https://github_kamoyl/kamoyl/AWS_automation/commit/3db6c431476496845b6b005dfaa5c310389db4e2) by Kamil Czarnecki).
- * updated gitignore ([1b6f465](https://github_kamoyl/kamoyl/AWS_automation/commit/1b6f465e4d2eb6c72cee7f1e17629cdfb5d9a1aa) by Kamil Czarnecki).
- * adding changelog ([2db1473](https://github_kamoyl/kamoyl/AWS_automation/commit/2db1473493a931b4d516f61158d010d2bb81db1c) by Kamil Czarnecki).
- * small correction of static value when sending slack ([c1aefbe](https://github_kamoyl/kamoyl/AWS_automation/commit/c1aefbef35be7909d9d79da5aeab2170da7e78d7) by Kamil Czarnecki).
- * added checking of S3 buckets features like secure access instead of apply it each time ([d6bba08](https://github_kamoyl/kamoyl/AWS_automation/commit/d6bba08bb43772be5d7d8bceb226bdf93e691042) by Kamil Czarnecki).
- * lambda is migrated to bash function, which let's now deploy more of them, related to evens by name ([bd373d1](https://github_kamoyl/kamoyl/AWS_automation/commit/bd373d17542a1fe6ecf2dbba9e7323541c80865e) by Kamil Czarnecki).
- * Added changelog ([64b466e](https://github_kamoyl/kamoyl/AWS_automation/commit/64b466e15b2c94340837c4f48bae2da0a5948316) by Kamil Czarnecki).
- * eventbridge attached - it is deployed right after lambda, and with lambda related ([d7ed0bf](https://github_kamoyl/kamoyl/AWS_automation/commit/d7ed0bf50d9464b09fa6587e30d4576c1ff8955c) by Kamil Czarnecki).
- * added checking mandatory aws cli ([4a09dcd](https://github_kamoyl/kamoyl/AWS_automation/commit/4a09dcd10b5b7fdcb6b7cc57856189f85f46d117) by Kamil Czarnecki).
- Initial commit ([a523402](https://github_kamoyl/kamoyl/AWS_automation/commit/a523402bebf0b125623026594c32ddacfca6270a) by Kamil Czarnecki).

<!-- insertion marker -->

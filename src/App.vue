<template>
  <div class="flex flex-col items-center">
    <div class="border-dotted border-2 border-blue-300 mb-4 mt-4">
      <img v-if="!imageLoaded" src="./assets/loading.gif" alt="Loading..." class="h-[70vh]" />
      <img v-else src="./assets/gab.gif" alt="Grad Pictures" class="h-[70vh]" />
    </div>

    <div class="flex h-10">
      <span class="font-bold text-xl font-mono">Gab's Grad Dedications</span>
    </div>
    <div class="flex h-10">
      <input
        type="password"
        v-model="code"
        class="w-40 h-full mr-2 px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-blue-500"
        placeholder="Enter your code"
      />
      <button
        type="button"
        class="h-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-white"
        @click="handleClick"
      >
        Submit
      </button>
    </div>
  </div>

  <TransitionRoot as="template" :show="open">
    <Dialog class="relative z-10">
      <TransitionChild
        as="template"
        enter="ease-in-out duration-500"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="ease-in-out duration-500"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 overflow-hidden">
        <div class="absolute inset-0 overflow-hidden">
          <div class="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10">
            <TransitionChild
              as="template"
              enter="transform transition ease-in-out duration-500 sm:duration-700"
              enter-from="translate-x-full"
              enter-to="translate-x-0"
              leave="transform transition ease-in-out duration-500 sm:duration-700"
              leave-from="translate-x-0"
              leave-to="translate-x-full"
            >
              <DialogPanel class="pointer-events-auto relative w-screen max-w-md">
                <TransitionChild
                  as="template"
                  enter="ease-in-out duration-500"
                  enter-from="opacity-0"
                  enter-to="opacity-100"
                  leave="ease-in-out duration-500"
                  leave-from="opacity-100"
                  leave-to="opacity-0"
                >
                  <div class="absolute left-0 top-0 -ml-8 flex pr-2 pt-4 sm:-ml-10 sm:pr-4">
                    <button
                      type="button"
                      class="relative rounded-md text-gray-300 hover:text-white focus:outline-none focus:ring-2 focus:ring-white"
                      @click="handleClick"
                    >
                      <span class="absolute -inset-2.5" />
                      <span class="sr-only">Close panel</span>
                      <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                    </button>
                  </div>
                </TransitionChild>
                <div class="flex h-full flex-col overflow-y-scroll bg-white py-6 shadow-xl">
                  <div class="px-4 sm:px-6">
                    <DialogTitle class="text-lg font-semibold leading-6 text-gray-900"
                      >Hello {{ curName }}!</DialogTitle
                    >
                  </div>
                  <div class="relative mt-6 flex-1 px-4 sm:px-6">{{ curMessage }}</div>
                  <div v-if="curName != 'there'" class="relative px-4 sm:px-6">
                    See all of my grad pics
                    <a
                      href="https://drive.google.com/drive/folders/13EkwpzWRE9AuBQRbS_1R0R9JgBpJ1SXq?usp=sharing"
                      target="_blank"
                      class="text-cyan-700 underline"
                      >here</a
                    >.
                  </div>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { XMarkIcon } from '@heroicons/vue/24/outline'
import axios from 'axios'

const open = ref(false)
const code = ref('')
const data = ref(null)
const curName = ref('')
const curMessage = ref('')

const imageLoaded = ref(false)

onMounted(() => {
  const timeout = Math.floor(Math.random() * 1500) + 1500
  setTimeout(() => {
    imageLoaded.value = true
  }, timeout)
})

const fetchData = async () => {
  try {
    const response = await axios.get(
      'https://raw.githubusercontent.com/H3XoRuSH/gab-grad-dedications/main/public/msgs/msgs.json'
    )
    const curData = response.data
    data.value = initData(curData)
  } catch (error) {
    console.error('Error fetching data:', error)
  }
}

const initData = (curData) => {
  var newData = {}
  for (let i = 0; i < curData.length; i++) {
    newData[curData[i].code] = {
      name: curData[i].name,
      message: curData[i].message
    }
  }
  return newData
}

fetchData()

const handleClick = () => {
  const openVal = open.value

  if (openVal == true) {
    open.value = false
    code.value = ''
  } else {
    open.value = true

    if (code.value in data.value) {
      curName.value = data.value[code.value].name
      curMessage.value = data.value[code.value].message
    } else {
      curName.value = 'there'
      curMessage.value =
        "It seems like I currently have no message for you. Please recheck the code I sent you! If it still fails or I have not sent you a code, I might have forgotten to create one, I'm sorry!"
    }
  }
}
</script>

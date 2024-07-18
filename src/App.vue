<template>
  <div class="flex flex-col items-center">
    <div class="border-dotted border-2 border-blue-300 mb-4 mt-4">
      <img src="./assets/gab.gif" alt="Grad Pictures" class="h-[70vh]" />
    </div>

    <div class="flex h-10">
      <span class="font-bold text-xl font-mono">Gab's Grad Dedications</span>
    </div>
    <div class="flex h-10">
      <input
        type="password"
        v-model="code"
        class="w-40 h-full mr-3 px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-blue-500"
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
    <Dialog class="fixed inset-0 z-10 overflow-y-auto">
      <div
        class="flex items-center justify-center min-h-screen px-4 pt-4 pb-20 text-center sm:block sm:p-0"
      >
        <TransitionChild
          as="template"
          enter="ease-out duration-300"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="ease-in duration-200"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div
            class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
            aria-hidden="true"
          ></div>
        </TransitionChild>

        <!-- This element is to trick the browser into centering the modal contents. -->
        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true"
          >&#8203;</span
        >

        <TransitionChild
          as="template"
          enter="ease-out duration-300"
          enter-from="opacity-0 scale-95"
          enter-to="opacity-100 scale-100"
          leave="ease-in duration-200"
          leave-from="opacity-100 scale-100"
          leave-to="opacity-0 scale-95"
        >
          <DialogPanel
            class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full"
          >
            <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
              <div class="sm:flex sm:items-start">
                <div class="sm:mt-0 sm:text-left">
                  <DialogTitle class="text-lg leading-6 font-medium text-gray-900">
                    Hello {{ curName }}!
                  </DialogTitle>
                  <div class="mt-3">
                    <p class="text-sm text-gray-500 text-justify">{{ curMessage }}</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:items-center">
              <div class="flex-1 text-sm text-gray-500">
                <p class="text-sm text-gray-500">
                  See all of my grad pics
                  <a
                    href="https://drive.google.com/drive/folders/13EkwpzWRE9AuBQRbS_1R0R9JgBpJ1SXq?usp=sharing"
                    target="_blank"
                    class="text-cyan-700 underline"
                    >here</a
                  >.
                </p>
              </div>
              <button
                type="button"
                class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm"
                @click="handleClick"
              >
                Close
              </button>
            </div>
          </DialogPanel>
        </TransitionChild>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import { ref } from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import axios from 'axios'

const open = ref(false)
const code = ref('')
const data = ref(null)
const curName = ref('')
const curMessage = ref('')

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

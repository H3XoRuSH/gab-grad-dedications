<template>
  <div class="flex justify-center">
    <input
      type="text"
      v-model="code"
      class="w-40 mr-2 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-blue-500"
      placeholder="Enter your code"
    />
    <button
      type="button"
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-white"
      @click="handleClick"
    >
      Submit
    </button>
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
                    <DialogTitle class="text-base font-semibold leading-6 text-gray-900"
                      >Hello {{ code }}!</DialogTitle
                    >
                  </div>
                  <div class="relative mt-6 flex-1 px-4 sm:px-6"></div>
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
import { ref } from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { XMarkIcon } from '@heroicons/vue/24/outline'

const open = ref(false)
const code = ref('')

const data = ref(null)
const fetchData = async () => {
  try {
    const response = await fetch(
      'https://raw.githubusercontent.com/H3XoRuSH/gab-grad-dedications/main/public/msgs/msgs.json'
    )
    if (!response.ok) {
      throw new Error(`Error fetching data: ${response.statusText}`)
    }
    const textData = await response.text()
    console.log(textData)
    // const jsonData = JSON.parse(textData)
    // data.value = jsonData
  } catch (error) {
    console.error('Error:', error)
  }
}

fetchData()

const handleClick = () => {
  const openVal = open.value

  if (openVal == true) {
    open.value = false
    code.value = ''
  } else {
    open.value = true
  }

  getMessage()
}

const getMessage = () => {
  console.log('test')
}
</script>

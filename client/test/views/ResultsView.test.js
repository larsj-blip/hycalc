import {flushPromises, mount} from '@vue/test-utils'
import {expect, test, vi, beforeAll, afterAll, afterEach} from 'vitest';
import {createTestingPinia} from '@pinia/testing'
import ResultsView from "@/views/ResultsView.vue";
import {server} from "../mocks/mock_server.js"
import {data} from "../mocks/handler.js";

beforeAll(() => server.listen({ onUnhandledRequest: 'error' }))
afterAll(() => server.close())
afterEach(() => server.resetHandlers())
test('table data is populated reactively', async () => {
  const wrapper = mount(ResultsView, {
    global: {
      plugins: [createTestingPinia(
        {
          createSpy: vi.fn,
          initialState: {
            form_store: { distance_traveled: 100 }
          }
        }
      )]
    }
  })

  let domWrapper = wrapper.find('button');
  await domWrapper.trigger("click",);
  await flushPromises()
  expect(wrapper.vm.refueling_data).toEqual(data)
})

test('table is populated with all data', async () => {
  const wrapper = mount(ResultsView, {
    global: {
      plugins: [createTestingPinia(
        {
          createSpy: vi.fn,
          initialState: {
            form_store: { distance_traveled: 100 }
          }
        }
      )]
    }
  })

  await flushPromises()
  let amount_of_components = wrapper.findAll('[data-test="result_row"]').length;
  expect(amount_of_components).toEqual(data.length)
})
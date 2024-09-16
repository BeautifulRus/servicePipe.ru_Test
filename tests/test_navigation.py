from asyncio import wait_for

import pytest
import allure
from playwright.sync_api import sync_playwright


@pytest.mark.parametrize("browser_name", ["chromium", "firefox"])
@pytest.mark.parametrize("resolution", ["1024x768"])
@pytest.mark.FLAKY #Поскольку, как я заметил, локаторы radix временами изменяются, и тест падает
@pytest.mark.gui
@pytest.mark.positive
def test_navigation(browser_name, resolution):
    with sync_playwright() as p:
        browser = p[browser_name].launch(headless=False)
        context = browser.new_context(viewport={"width": 1024, "height": 768})
        page = context.new_page()

        with allure.step("Шаг 1: Открыть сайт"):
            page.goto("https://servicepipe.ru/")

        with allure.step("Шаг 2: Нажать на кнопку, открывающую списки"):
            page.click('//*[@id="__next"]/nav/header/div/div[3]/nav/div[2]/button') #Без успешного клика тест упадёт

        # Создаем словарь с ожидаемыми ссылками
        expected_links = {
            "Решения": {
                "/finance": '//*[@id="radix-:r1:"]/div/div/div[1]/div[2]/div[1]/a',
                "/retail":  '//*[@id="radix-:r1:"]/div/div/div[1]/div[2]/div[2]/a',
                "/marketing": '//*[@id="radix-:r1:"]/div/div/div[1]/div[2]/div[3]/a',
                "/web":     '//*[@id="radix-:r1:"]/div/div/div[2]/div[2]/div[1]/a',
                "/network": '//*[@id="radix-:r1:"]/div/div/div[2]/div[2]/div[2]/a',
                "/audit":   '//*[@id="radix-:r1:"]/div/div/div[2]/div[2]/div[3]/a',
            },
            "Технологии": {
                "/flowcollector": '//*[@id="radix-:r2:"]/div/div/div/div/div[1]/a',
                "/dosgate":       '//*[@id="radix-:r2:"]/div/div/div/div/div[2]/a',
                "/cybert":        '//*[@id="radix-:r2:"]/div/div/div/div/div[3]/a',
            },
            "Продукты": {
                "/web/ddos-protection": '//*[@id="radix-:r4:"]/div/div/div/div/div[1]/a',
                "/web/bot-protection": '//*[@id="radix-:r4:"]/div/div/div/div/div[2]/a',
                "/web/bot-checks": '//*[@id="radix-:r4:"]/div/div/div/div/div[3]/a',
                "/web/waf": '//*[@id="radix-:r4:"]/div/div/div/div/div[4]/a',
                "/network/ip-transit": '//*[@id="radix-:r4:"]/div/div/div/div/div[5]/a',
                "/network/cloud-firewall": '//*[@id="radix-:r4:"]/div/div/div/div/div[6]/a',
                "/network/slave-dns": '//*[@id="radix-:r4:"]/div/div/div/div/div[7]/a',
                "/audit/stress-test": '//*[@id="radix-:r4:"]/div/div/div/div/div[7]/a',
            }
            ,
            "О компании": {
                "/about": '//*[@id="radix-:rq:"]/div/div/div/div/div[1]/a',
                "/career": '//*[@id="radix-:rq:"]/div/div/div/div/div[2]/a',
                "/contacts": '//*[@id="radix-:rq:"]/div/div/div/div/div[3]/a',
                "/press-center": '//*[@id="radix-:rq:"]/div/div/div/div/div[4]/a',
                "/why-servicepipe": '//*[@id="radix-:rq:"]/div/div/div/div/div[5]/a',
                "/partners": '//*[@id="radix-:rq:"]/div/div/div/div/div[6]/a',


            },

        }

        # Проверяем ссылки "Решения"
        with allure.step('Шаг 3: Нажать на список "Решения"'):
            page.click('//*[@id="radix-:r0:"]')
            page.wait_for_timeout(1000)
            assert page.get_attribute('//*[@id="radix-:Rkl6:"]/div[2]/div/div/div/div/div[1]/div[2]/div[1]',
                                      'data-state') == "open"


        with allure.step("Шаг 4: Проверить ссылки из списка \"Решения\" на корректность"):
            for name, selector in expected_links["Решения"].items():
                link = page.query_selector(selector)
                if link:
                    url = link.get_attribute("href")
                    expected_url = name
                    assert url.endswith(expected_url), f'Expected URL: {expected_url}, but got: {url}'

        # Проверяем ссылки "Технологии"
        with allure.step('Шаг 5: Нажать на список "Технологии"'):
            page.click('//*[@id="radix-:r2:"]')
            page.wait_for_timeout(1000)
            assert page.get_attribute('//*[@id="radix-:Rkl6:"]/div[2]/div/div/div/div/div[1]/div[2]/div[2]',
                                      'data-state') == "open"

        with allure.step("Шаг 6: Проверить ссылки из списка \"Технологии\" на корректность"):
            for name, selector in expected_links["Технологии"].items():
                link = page.query_selector(selector)
                if link:
                    url = link.get_attribute("href")
                    expected_url = name
                    assert url.endswith(expected_url), f'Expected URL: {expected_url}, but got: {url}'




            # Проверяем ссылки "Продукты"
        with allure.step('Шаг 7: Нажать на список "Продукты"'):
            page.click('//*[@id="radix-:r4:"]')
            page.wait_for_timeout(1000)
            assert page.get_attribute('//*[@id="radix-:Rkl6:"]/div[2]/div/div/div/div/div[1]/div[2]/div[3]',
                                      'data-state') == "open"

        with allure.step("Шаг 8: Проверить ссылки из списка \"Продукты\" на корректность"):
            for name, selector in expected_links["Продукты"].items():
                link = page.query_selector(selector)
                if link:
                    url = link.get_attribute("href")
                    expected_url = name
                    assert url.endswith(expected_url), f'Expected URL: {expected_url}, but got: {url}'


          # Проверяем ссылки "О компании"
        with allure.step('Шаг 9: Нажать на список "О компании"'):
            page.click('//*[@id="radix-:r6:"]')
            page.wait_for_timeout(1000)
            assert page.get_attribute('//*[@id="radix-:r6:"]', #сменил локатор, поскольку он иногда изменяется
                                      'data-state') == "open" #ТЕСТ FLAKY

        with allure.step("Шаг 10: Проверить ссылки из списка \"О компании\" на корректность"):
            for name, selector in expected_links["О компании"].items():
                link = page.query_selector(selector)
                if link:
                    url = link.get_attribute("href")
                    expected_url = name
                    assert url.endswith(expected_url), f'Expected URL: {expected_url}, but got: {url}'



        context.close()
        browser.close()













@pytest.mark.parametrize("browser_name", ["chromium", "firefox"])
@pytest.mark.parametrize("resolution", ["1024x768"])
@pytest.mark.gui
@pytest.mark.positive
def test_navigation_endScroll(browser_name, resolution):
    with sync_playwright() as p:
        browser = p[browser_name].launch(headless=False)
        context = browser.new_context(viewport={"width": 1024, "height": 768})
        page = context.new_page()

        with allure.step("Шаг 1: Открыть сайт"):
            page.goto("https://servicepipe.ru/")

        # Создаем словарь с ожидаемыми ссылками
        expected_links = {
            "Все ссылки внизу страницы": {

                #Решения
                "/web": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/a[1]',
                "/network": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/a[2]',
                "/audit": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/a[3]',
                "/finance": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/a[4]',
                "/retail": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/a[5]',
                "/marketing": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/a[6]',

                #Технологии
                "/flowcollector": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/a[1]',
                "/dosgate": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/a[2]',
                "/cybert": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/a[3]',

                #Продукты
                "/web/ddos-protection": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/a[1]',
                "/web/bot-protection": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/a[2]',
                "/web/bot-checks": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/a[3]',
                "/web/waf": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/a[4]',
                "/network/ip-transit": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/a[5]',
                "/network/cloud-firewall": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/a[6]',
                "/network/slave-dns": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/a[7]',
                "/audit/stress-test": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/a[8]',

                #О компании
                "/about": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/a[1]',
                "/career": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/a[2]',
                "/contacts": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/a[3]',
                "/press-center": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/a[4]',
                "/why-servicepipe": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/a[5]',
                "/partners": '//*[@id="footer"]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/a[6]',

                #Оставшиеся ссылки
                "": '//*[@id="footer"]/div/div/div[1]/div[1]/div[1]/div/div[1]/a', #лого компании
                #"https://navigator.sk.ru/orn/1124299?roistat_visit=268044": '//*[@id="footer"]/div/div/div[1]/div[1]/div[1]/div/div[2]/a', #лого SkУчастник
                #"tel:+74996817548": '//*[@id="footer"]/div/div/div[1]/div[1]/div[4]/div[1]/a', #телефон
                "mailto:welcome@servicepipe.ru": '//*[@id="footer"]/div/div/div[1]/div[1]/div[4]/div[2]/a', #почта
                #"https://vk.com/official_servicepipe?roistat_visit=268044": '//*[@id="footer"]/div/div/div[1]/div[1]/div[4]/div[2]/div/a[1]', #вк
                #"https://t.me/official_servicepipe?roistat_visit=268044": '//*[@id="footer"]/div/div/div[1]/div[1]/div[4]/div[2]/div/a[2]', #тг
                "https://servicepipe.ru/uploads/SP_Personal_data_processing_policy_38a7b37f69.pdf": '//*[@id="footer"]/div/div/div[2]/div[2]/div/a', #Политика конфиденциальности
                #"https://lvmd.ru/?roistat_visit=268044": '//*[@id="footer"]/div/div/div[2]/div[3]/div/a', #Дизайн сайта — lovemedo
                # часть после "=" изменяется каждый раз. пока не знаю простого решения. пока закоментил
                # номер телефона тоже динамически изменяется. пока закоментил

            }
        }

        # Проверяем ссылки
        with allure.step("Шаг 2: Проверить все ссылки внизу страницы на корректность"):
            for name, selector in expected_links["Все ссылки внизу страницы"].items():
                link = page.query_selector(selector)
                if link:
                    url = link.get_attribute("href")
                    expected_url = name
                    assert url.endswith(expected_url), f'Expected URL: {expected_url}, but got: {url}'

        context.close()
        browser.close()






@pytest.mark.parametrize("browser_name", ["chromium", "firefox"])
@pytest.mark.parametrize("resolution", ["1024x768"])
@pytest.mark.gui
@pytest.mark.positive
def test_navigation_scrollToFormOnDemoProduct(browser_name, resolution):
    with sync_playwright() as p:
        browser = p[browser_name].launch(headless=False)
        context = browser.new_context(viewport={"width": 1024, "height": 768})
        page = context.new_page()

        with allure.step("Шаг 1: Открыть сайт"):
            page.goto("https://servicepipe.ru/")


        with allure.step('Шаг 2: Нажать на кнопку "Попробовать бесплатно"'):
            page.click()
            # page.click('//*[@id="main"]/div[2]/div[1]/div/div/div/div/div/div[1]/button')
        # не придумал как проверить правильность скрола в конец страницы


        context.close()
        browser.close()

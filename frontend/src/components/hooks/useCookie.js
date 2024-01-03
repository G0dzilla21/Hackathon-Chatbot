// src/hooks/useCookie.js
import { useCallback } from 'react';
import Cookies from 'js-cookie';

const useCookie = () => {
    const getCookie = useCallback((name) => {
        return Cookies.get(name);
    }, []);

    const setCookie = useCallback((name, value, options) => {
        Cookies.set(name, value, options);
    }, []);

    const deleteCookie = useCallback((name) => {
        Cookies.remove(name);
    }, []);

    return { getCookie, setCookie, deleteCookie };
};

export default useCookie;

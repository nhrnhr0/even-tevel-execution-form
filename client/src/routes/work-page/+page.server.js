import { CATEGORY_URL, WEIGHT_RATIO_URL } from '../../lib/consts.js';

/**
 * Load categories and weights from the specified URLs.
 * @returns {Promise<{ categories: any, weights: any }>} - Object containing categories and weights.
 */
export async function load(event) {
    try {
        console.log(CATEGORY_URL);

        const [categoriesResponse, weightsResponse] = await Promise.all([
            event.fetch(CATEGORY_URL),
            event.fetch(WEIGHT_RATIO_URL)
        ]);

        if (!categoriesResponse.ok || !weightsResponse.ok) {
            throw new Error('Failed to fetch data.');
        }

        // const categories = await categoriesResponse.json();
        // const weights = await weightsResponse.json();
        let categories, weights;
        [categories, weights] = await Promise.all([
            categoriesResponse.json(),
            weightsResponse.json()
        ]);

        return { categories, weights };
    } catch (error) {
        console.error('An error occurred:', error);
        throw error; // Re-throw the error for upper layers to handle
    }
}

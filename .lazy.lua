return {
	{
		"folke/snacks.nvim",
		opts = { picker = { sources = { explorer = { diagnostics = false } } } },
	},
	{
		"neovim/nvim-lspconfig",
		opts = { diagnostics = { virtual_text = false, underline = false, signs = false } },
	},
	{
		"akinsho/bufferline.nvim",
		opts = { options = { diagnostics = false } },
	},
}
